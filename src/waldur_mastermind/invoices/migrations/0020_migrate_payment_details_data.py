# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 13:07
from __future__ import unicode_literals

import logging

from django.db import migrations

from waldur_core.core import fields


logger = logging.getLogger(__name__)


def migrate_data(apps, schema_editor):
    PaymentDetails = apps.get_model('invoices', 'PaymentDetails')
    properties = [
        ['_company', 'name'],
        ['_type', 'type'],
        ['_address', 'address'],
        ['_country', 'country'],
        ['_email', 'email'],
        ['_postal', 'postal'],
        ['_phone', 'phone_number'],
        ['_bank', 'bank_name'],
        ['_account', 'bank_account'],
        ['_accounting_start_date', 'accounting_start_date'],
        ['_default_tax_percent', 'default_tax_percent'],
    ]
    
    for pd in PaymentDetails.objects.all():
        
        for p in properties:
            value_payment = getattr(pd, p[0])
            value_customer = getattr(pd.customer, p[1])

            if p[1] in ['accounting_start_date', 'default_tax_percent'] and value_payment:
                setattr(pd.customer, p[1], value_payment)
                continue

            if not value_customer and value_payment:
                if not p[1] == 'country':
                    setattr(pd.customer, p[1], value_payment)
                else:
                    country = filter(lambda x: x[1] == value_payment, fields.CountryField.COUNTRIES)
                    if country:
                        setattr(pd.customer, p[1], country[0][0])
                    else:
                        logger.warning('Migrate payment details data. Invalid country name %s' % value_payment)
                
        pd.customer.save()


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0019_mark_payments_details_fields'),
        ('structure', '0054_payment_details'),
    ]

    operations = [
        migrations.RunPython(migrate_data, reverse_code=migrations.RunPython.noop, elidable=True),
    ]
