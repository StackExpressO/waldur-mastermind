# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-09 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0041_tenant_default_volume_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnet',
            name='disable_gateway',
            field=models.BooleanField(default=False),
        ),
    ]