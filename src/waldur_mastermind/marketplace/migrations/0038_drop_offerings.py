# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-02 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def cleanup_all_offerings(apps, schema_editor):
    Offering = apps.get_model('marketplace', 'Offering')
    Offering.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0037_component_usage'),
    ]

    operations = [
        migrations.RunPython(cleanup_all_offerings, elidable=True),
    ]
