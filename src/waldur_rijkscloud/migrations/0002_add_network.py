# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_squashed_0054'),
        ('waldur_rijkscloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloatingIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('address', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('is_available', models.BooleanField(default=True)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'verbose_name': 'Floating IP',
                'verbose_name_plural': 'Floating IPs',
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InternalIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('address', models.GenericIPAddressField(protocol='IPv4')),
                ('is_available', models.BooleanField(default=True)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'verbose_name': 'Internal IP',
                'verbose_name_plural': 'Internal IPs',
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SubNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                ('cidr', models.CharField(max_length=32)),
                ('gateway_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('allocation_pools', waldur_core.core.fields.JSONField()),
                ('dns_nameservers', waldur_core.core.fields.JSONField(help_text='List of DNS name servers associated with the subnet.')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subnets', to='waldur_rijkscloud.Network')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings')),
            ],
            options={
                'verbose_name': 'Subnet',
                'verbose_name_plural': 'Subnets',
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='internalip',
            name='subnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internal_ips', to='waldur_rijkscloud.SubNet'),
        ),
        migrations.AddField(
            model_name='instance',
            name='floating_ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waldur_rijkscloud.FloatingIP'),
        ),
        migrations.AddField(
            model_name='instance',
            name='internal_ip',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_rijkscloud.InternalIP'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='subnet',
            unique_together=set([('settings', 'backend_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='network',
            unique_together=set([('settings', 'backend_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='internalip',
            unique_together=set([('settings', 'backend_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='floatingip',
            unique_together=set([('settings', 'backend_id')]),
        ),
    ]