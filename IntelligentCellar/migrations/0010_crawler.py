# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntelligentCellar', '0009_auto_20160126_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cup', models.CharField(max_length=30)),
            ],
        ),
    ]
