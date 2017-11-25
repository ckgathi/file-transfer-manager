from django.db import models


class HostModelMixin:

    name = models.CharField(
        verbose_name="File name",
        max_length=250)

    sftp_url = models.CharField(
        verbose_name="SFTP Server url or IP Address",
        max_length=250)

    sftp_user = models.CharField(
        verbose_name="SFTP Username",
        max_length=100)

    sftp_pass = models.CharField(
        verbose_name="SFTP Password",
        max_length=100)

    active = models.BooleanField(
        default=False,
        verbose_name="Client active status",)

    ping = models.BooleanField(
        default=False)

    site_group_name = models.CharField(
        verbose_name="Site group name",
        max_length=250,
        null=True)
