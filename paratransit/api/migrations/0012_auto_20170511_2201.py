# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_dropoff_locations_pickup_locations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dropoff_locations',
            old_name='p_lat',
            new_name='d_lat',
        ),
        migrations.RenameField(
            model_name='dropoff_locations',
            old_name='p_lng',
            new_name='d_lng',
        ),
        migrations.RenameField(
            model_name='dropoff_locations',
            old_name='point',
            new_name='the_geom',
        ),
        migrations.RenameField(
            model_name='pickup_locations',
            old_name='point',
            new_name='the_geom',
        ),
    ]
