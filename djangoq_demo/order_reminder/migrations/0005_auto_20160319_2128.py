# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_reminder', '0004_auto_20160318_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
