# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-10 12:58
from __future__ import unicode_literals

from django.db import migrations
import nodeconductor.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0007_add_details_to_expertrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertrequest',
            name='extra',
            field=nodeconductor.core.fields.JSONField(default={}),
        ),
    ]