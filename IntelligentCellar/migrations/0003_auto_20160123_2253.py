# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IntelligentCellar', '0002_auto_20160123_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='requestTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
