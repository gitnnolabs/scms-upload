from django.utils.translation import gettext as _

from packtools.sps import sps_maker

from article.controller import create_article_from_etree
from article.models import Article
from config import celery_app
from libs.dsm.publication.db import mk_connection, exceptions
from libs.dsm.publication.documents import get_document
from upload.models import Package
from upload.choices import PC_ERRATUM, PC_CORRECTION

from .utils import file_utils, package_utils, xml_utils
from . import choices, controller


def run_validations(filename, package_id, package_category, article_id=None):
    if article_id is not None and package_category in (PC_CORRECTION, PC_ERRATUM):
        task_validate_article_change(filename, package_id, package_category, article_id)
    else:
        xml_format_is_valid = task_validate_xml_format(filename, package_id)

        if xml_format_is_valid:
            optimised_filepath = task_optimise_package(filename)

            task_validate_assets.apply_async(kwargs={'file_path': optimised_filepath, 'package_id': package_id}, countdown=10)
            task_validate_renditions.apply_async(kwargs={'file_path': optimised_filepath, 'package_id': package_id}, countdown=10)


def check_resolutions(package_id):
    task_check_resolutions.apply_async(kwargs={'package_id': package_id}, countdown=3)


def check_opinions(package_id):
    task_check_opinions.apply_async(kwargs={'package_id': package_id}, countdown=3)


def get_or_create_package(article_id, pid, user_id):
    task_result = task_get_or_create_package.apply_async(kwargs={'article_id': article_id, 'pid': pid, 'user_id': user_id})
    return task_result.get()



@celery_app.task(name='Validate article change')
def task_validate_article_change(file_path, package_id, package_type, article_id):
    if package_type == PT_CORRECTION:
        task_validate_article_correction.apply_async(kwargs={'file_path': file_path, 'package_id': package_id, 'article_id': article_id})
    elif package_type == PT_ERRATUM:
        task_validate_article_erratum.apply_async(kwargs={'file_path': file_path, 'package_id': package_id, 'article_id': article_id})
        # TODO: comparar dados de XML corrigido com aqueles do pacote baixado para gerar a correção, task_compare_article_erratum_with_last_package()


@celery_app.task(name='Validate article correction')
def task_validate_article_correction(file_path, package_id, article_id):
    # TODO: aguardar update do packtools
    # pkg_with_correction = PackageWithCorrection(file_path)
    # return pkg_with_correction.is_valid()
    ...


@celery_app.task(name='Validate article erratum')
def task_validate_article_erratum(file_path, package_id, article_id):
    # TODO: aguardar update do packtools
    # pkg_with_errata = PackageWithErrata(file_path)
    # return pkg_with_errata.is_valid()
    ...


@celery_app.task()
def task_validate_xml_format(file_path, package_id):
    try:
        xml_str = file_utils.get_xml_content_from_zip(file_path)
        xml_utils.get_etree_from_xml_content(xml_str)
        return True

    except (file_utils.BadPackageFileError, file_utils.PackageWithoutXMLFileError):
        controller.add_validation_error(
            choices.VE_PACKAGE_FILE_ERROR,
            package_id,
            choices.PS_REJECTED
        )

    except xml_utils.XMLFormatError as e:
        data = {
            'column': e.column,
            'row': e.start_row,
            'snippet': xml_utils.get_snippet(xml_str, e.start_row, e.end_row),
        }

        controller.add_validation_error(
            choices.VE_XML_FORMAT_ERROR,
            package_id,
            choices.PS_REJECTED,
            message=e.message,
            data=data,
        )

    return False


@celery_app.task()
def task_optimise_package(file_path):
    source = file_utils.get_file_absolute_path(file_path)
    target = file_utils.generate_filepath_with_new_extension(source, '.optz', True)
    package_utils.optimise_package(source, target)
    package_utils.unzip(target)

    return target


@celery_app.task()
def task_validate_assets(file_path, package_id):
    package_files = file_utils.get_file_list_from_zip(file_path)
    article_assets = package_utils.get_article_assets_from_zipped_xml(file_path)

    for asset_result in package_utils.evaluate_assets(article_assets, package_files):
        asset, is_present = asset_result

        if not is_present:
            controller.add_validation_error(
                choices.VE_ASSET_ERROR,
                package_id,
                choices.PS_REJECTED,
                message=f'{asset.name} {_("file is mentioned in the XML but not present in the package.")}',
                data={
                    'id': asset.id,
                    'type': asset.type,
                    'missing_file': asset.name,
                },
            )

            controller.add_validation_error(
                choices.VE_ASSET_ERROR,
                package_id,
                choices.PS_REJECTED,
                message=f'{asset.name} {_("file is mentioned in the XML but its optimised version not present in the package.")}',
                data={
                    'id': asset.id,
                    'type': 'optimised',
                    'missing_file': file_utils.generate_filepath_with_new_extension(asset.name, '.png'),
                },
            )

            controller.add_validation_error(
                choices.VE_ASSET_ERROR,
                package_id,
                choices.PS_REJECTED,
                message=f'{asset.name} {_("file is mentioned in the XML but its thumbnail version not present in the package.")}',
                data={
                    'id': asset.id,
                    'type': 'thumbnail',
                    'missing_file': file_utils.generate_filepath_with_new_extension(asset.name, '.thumbnail.jpg'),
                },
            )


@celery_app.task()
def task_validate_renditions(file_path, package_id):
    package_files = file_utils.get_file_list_from_zip(file_path)
    article_renditions = package_utils.get_article_renditions_from_zipped_xml(file_path)

    for rendition_result in package_utils.evaluate_renditions(article_renditions, package_files):
        rendition, expected_filename, is_present = rendition_result

        if not is_present:
            controller.add_validation_error(
                choices.VE_RENDITION_ERROR,
                package_id,
                choices.PS_REJECTED,
                message=f'{rendition.language} {_("language is mentioned in the XML but its PDF file not present in the package.")}',
                data={
                    'language': rendition.language,
                    'is_main_language': rendition.is_main_language,
                    'missing_file': expected_filename,
                },
            )


@celery_app.task()
def task_check_resolutions(package_id):
    controller.update_package_check_errors(package_id)


@celery_app.task()
def task_check_opinions(package_id):
    controller.update_package_check_opinions(package_id)


@celery_app.task(name=_('Get or create package'))
def task_get_or_create_package(article_id, pid, user_id):
    try:
        # Tries to connect to site database (opac.article)
        mk_connection()
    except exceptions.DBConnectError:
        return {'error': _('Site database is unavailable.')}

    if article_id:
        article_inst = Article.objects.get(pk=article_id)
        doc = get_document(aid=article_inst.pid_v3)
    elif pid:
        doc = get_document(aid=pid)
        if doc.aid is not None:
            try:
                article_inst = Article.objects.get(pid_v3=doc.aid)
            except Article.DoesNotExist:
                xml_content = file_utils.get_xml_content_from_uri(doc.xml)
                xml_etree = package_utils.get_etree_from_xml_content(xml_content)
                article_inst = create_article_from_etree(xml_etree, user_id)

    if doc.aid is None:
        return {'error': _('It was not possible to retrieve a valid article.')}

    try:
        return Package.objects.get(article__pid_v3=article_inst.pid_v3).id
    except Package.DoesNotExist:
        # Retrieves PDF uris and names
        rend_uris_names = []
        for rend in doc.pdfs:
            rend_uris_names.append({
                'uri': rend['url'],
                'name': rend['filename'],
            })

        # Creates a zip file
        pkg_metadata = sps_maker.make_package_from_uris(
            xml_uri=doc.xml,
            renditions_uris_and_names=rend_uris_names, 
            zip_folder=file_utils.FileSystemStorage().base_location,
        )

        # Creates a package record
        pkg = controller.create_package(
            article_id=article_inst.id, 
            user_id=user_id, 
            file_name=file_utils.os.path.basename(pkg_metadata['zip']),
        )

        return pkg.id
