# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_project_is_removed'),
        ('openstack_tenant', '0043_field_availability_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceAvailabilityZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='instance',
            name='availability_zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openstack_tenant.InstanceAvailabilityZone'),
        ),
        migrations.AlterUniqueTogether(
            name='instanceavailabilityzone',
            unique_together=set([('settings', 'name')]),
        ),
    ]