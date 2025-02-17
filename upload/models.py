from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from core.models import CommonControlField

from . import choices
from .forms import UploadPackageForm
from .permission_helper import FINISH_DEPOSIT
from .utils import file_utils


class Package(CommonControlField):
    file = models.FileField(_('Package File'), null=True, blank=True)
    signature = models.CharField(_('Signature'), max_length=32, null=True, blank=True)
    status = models.CharField(_('Status'), max_length=32, choices=choices.PACKAGE_STATUS, default=choices.PS_ENQUEUED_FOR_VALIDATION)

    panels = [
        FieldPanel('file'),
    ]

    def __str__(self):
        return self.file.name

    def files_list(self):
        files = {'files': []}

        try:
            files.update({'files': file_utils.get_file_list_from_zip(self.file.path)})
        except file_utils.BadPackageFileError:
            # É preciso capturar esta exceção para garantir que aqueles que 
            #  usam files_list obtenham, na pior das hipóteses, um dicionário do tipo {'files': []}.
            # Isto pode ocorrer quando o zip for inválido, por exemplo.
            ...

        return files

    base_form_class = UploadPackageForm

    class Meta:
        permissions = (
            (FINISH_DEPOSIT, _("Can finish deposit")),
        )


class ValidationError(models.Model):
    category = models.CharField(_('Category'), max_length=32, choices=choices.VALIDATION_ERROR_CATEGORY, null=False, blank=False)

    row = models.PositiveIntegerField(_('Row'), null=True, blank=True)
    column = models.PositiveIntegerField(_('Column'), null=True, blank=True)
    message = models.CharField(_('Message'), max_length=128, null=True, blank=True)
    snippet = models.TextField(_('Snippet'), max_length=255, null=True, blank=True)

    package = models.ForeignKey('Package', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '-'.join([
            str(self.id),
            self.package.file.name,
            self.category,
        ])

    def get_standardized_category_label(self):
        return self.category.lower().replace('-', '_')

    # TODO: terá uma chave estrageira para um novo modelo chamado ValidationFeedback
    
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('package'),
                FieldPanel('category'),
                FieldPanel('column'),
                FieldPanel('row'),
            ],
            heading=_('Identification'),
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('message'),
                FieldPanel('snippet'),
            ],
            heading=_('Content'),
            classname='collapsible'
        )
    ]
