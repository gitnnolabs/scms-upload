from django.db import models
from django.utils.translation import gettext_lazy as _

from core.forms import CoreAdminModelForm
from core.models import CommonControlField
from collection.models import (
    ClassicWebsiteConfiguration,
    NewWebSiteConfiguration,
    FilesStorageConfiguration,
)

from . import choices


class MigrationConfiguration(CommonControlField):

    classic_website_config = models.ForeignKey(
        ClassicWebsiteConfiguration, on_delete=models.CASCADE)
    new_website_config = models.ForeignKey(
        NewWebSiteConfiguration, on_delete=models.CASCADE)
    files_storage_config = models.ForeignKey(
        FilesStorageConfiguration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.classic_website_config}"

    class Meta:
        indexes = [
            models.Index(fields=['classic_website_config']),
        ]

    base_form_class = CoreAdminModelForm


class MigratedData(CommonControlField):

    # datas no registro da base isis para identificar
    # se houve mudança nos dados durante a migração
    isis_updated_date = models.CharField(
        _('ISIS updated date'), max_length=8, null=True, blank=True)
    isis_created_date = models.CharField(
        _('ISIS created date'), max_length=8, null=True, blank=True)

    # dados migrados
    data = models.JSONField(blank=False, null=False)

    # status da migração
    status = models.CharField(
        _('Status'), max_length=20,
        choices=choices.MIGRATION_STATUS,
        default=choices.MS_TO_MIGRATE,
    )


class MigrationFailure(CommonControlField):
    pid = models.CharField(
        _('Item PID'), max_length=23, null=False, blank=False)
    exception_type = models.CharField(
        _('Exception Type'), max_length=255, null=False, blank=False)
    exception_msg = models.CharField(
        _('Exception Msg'), max_length=255, null=False, blank=False)
    action_name = models.CharField(
        _('Action'), max_length=255, null=False, blank=False)
    object_name = models.CharField(
        _('Object'), max_length=255, null=False, blank=False)
