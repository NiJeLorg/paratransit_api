# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170502_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='drophousenumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trips',
            name='pickhousenumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
