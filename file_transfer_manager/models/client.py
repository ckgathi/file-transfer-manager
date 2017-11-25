from edc_base.model_mixins import BaseUuidModel
from django.db import models

from .client_model_mixin import ClientModelMixin
from .host_model_mixin import HostModelMixin


class Client(HostModelMixin, ClientModelMixin, BaseUuidModel):

    has_files = models.BooleanField(
        default=False)

    remote_dirname = models.CharField(
        verbose_name="Client monitored directory",
        max_length=250,
        null=True)

    def __str__(self):
        return f'{self.sftp_url} {self.site_group_name}'

    class Meta:
        app_label = 'file_transfer_manager'
        unique_together = (
            ('sftp_url', 'remote_dirname'))
