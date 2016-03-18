# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField()),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer', models.CharField(max_length=200, null=True, unique=True, verbose_name=b'Company Name')),
                ('ship_date', models.DateField(help_text=b'Please use the following format: YYYY/MM/DD.', null=True)),
            ],
        ),
    ]
