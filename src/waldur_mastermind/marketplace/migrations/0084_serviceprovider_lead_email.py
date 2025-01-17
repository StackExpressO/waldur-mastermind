# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0083_offering_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='lead_email',
            field=models.EmailField(blank=True, max_length=254, null=True,
                                    help_text='Email for notification about new request based order items. If this field is set, notifications will be sent.'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='lead_body',
            field=models.TextField(blank=True, help_text='Notification body template. Django template variables can be used.'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='lead_subject',
            field=models.CharField(blank=True, max_length=255, help_text='Notification subject template. Django template variables can be used.'),
        ),
    ]
