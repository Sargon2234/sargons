# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='provider',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
