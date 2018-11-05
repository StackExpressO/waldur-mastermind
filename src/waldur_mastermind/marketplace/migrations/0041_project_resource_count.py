# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-05 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_immutable_default_json'),
        ('marketplace', '0040_categorycolumn'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectResourceCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='marketplace.Category')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectresourcecount',
            unique_together=set([('project', 'category')]),
        ),
    ]