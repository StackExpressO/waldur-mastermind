# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-11 11:40
from __future__ import unicode_literals

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0014_unique_package_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagetemplate',
            name='unit',
            field=models.CharField(choices=[('month', 'Per month'), ('half_month', 'Per half month'), ('day', 'Per day'), ('hour', 'Per hour'), ('quantity', 'Quantity')], default='day', max_length=30),
        ),
        migrations.AlterField(
            model_name='packagecomponent',
            name='price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Price per unit'),
        ),
    ]
