# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20180107_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsetting',
            name='text',
            field=models.TextField(),
        ),
    ]
