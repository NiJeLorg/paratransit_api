# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170413_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='d_geoid_tr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trips',
            name='geoid_pair',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trips',
            name='p_geoid_tr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
