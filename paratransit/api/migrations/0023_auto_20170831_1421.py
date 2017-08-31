# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-31 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_trips_pickup_dropoff_tracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips_pickup_dropoff_tracts',
            name='dropoff_tract',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trips_pickup_dropoff_tracts',
            name='pickup_tract',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
