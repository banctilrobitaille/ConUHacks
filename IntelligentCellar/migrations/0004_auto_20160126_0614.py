# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntelligentCellar', '0003_auto_20160123_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='size',
            field=models.CharField(max_length=20),
        ),
    ]
