from edc_base.model_mixins import BaseUuidModel
from django.db import models

from .client import Client
from .server import Server


class File(BaseUuidModel):

    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    server = models.ForeignKey(Server, on_delete=models.PROTECT)

    name = models.CharField(
        verbose_name="File name",
        max_length=250)

    client_name = models.CharField(
        verbose_name="Client name",
        max_length=250)

    server_name = models.CharField(
        verbose_name="Server name",
        max_length=250)

    def __str__(self):
        return f'{self.name} {self.client_name} {self.server_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.client_name = self.client.name
            self.server_name = self.server.name
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'file_transfer_manager'
        unique_together = (
            ('name', 'client_name', 'server_name'))
