# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 17:10
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20170711_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='nyc_odp_borough_boundaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_leng', models.FloatField()),
                ('boro_name', models.CharField(max_length=254)),
                ('boro_code', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]