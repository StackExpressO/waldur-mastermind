# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-10 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_vmware', '0011_add_datastore'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='disk',
            field=models.PositiveIntegerField(default=0, help_text='Disk size in MiB'),
        ),
    ]
