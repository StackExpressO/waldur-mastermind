# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-27 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0092_improve_internal_name_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeringcomponent',
            name='max_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='offeringcomponent',
            name='min_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
