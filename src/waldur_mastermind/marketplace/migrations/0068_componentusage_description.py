# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-27 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0067_offeringcomponent_disable_quotas'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentusage',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='description'),
        ),
    ]
