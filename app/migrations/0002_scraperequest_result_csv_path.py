# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraperequest',
            name='result_csv_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]