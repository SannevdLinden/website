# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180104_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depthdata',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
