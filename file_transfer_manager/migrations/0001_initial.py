# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 00:37
from __future__ import unicode_literals

import _socket
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='File name')),
                ('sftp_url', models.CharField(max_length=250, verbose_name='SFTP Server url or IP Address')),
                ('sftp_user', models.CharField(max_length=100, verbose_name='SFTP Username')),
                ('sftp_pass', models.CharField(max_length=100, verbose_name='SFTP Password')),
                ('active', models.BooleanField(default=False, verbose_name='Client active status')),
                ('has_files', models.BooleanField(default=False)),
                ('ping', models.BooleanField(default=False)),
                ('remote_dirname', models.CharField(max_length=250, null=True, verbose_name='Client monitored directory')),
                ('site_group_name', models.CharField(max_length=250, null=True, verbose_name='Site group name')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='File name')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='file_transfer_manager.Client')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set([('sftp_url', 'remote_dirname')]),
        ),
    ]