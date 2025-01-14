# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-27 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_vmware', '0020_guest_power_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='tools_state',
            field=models.CharField(blank=True, choices=[('STARTING', 'Starting'), ('RUNNING', 'Running'), ('NOT_RUNNING', 'Not running')], max_length=50, verbose_name='Current running status of VMware Tools running in the guest operating system.'),
        ),
    ]
