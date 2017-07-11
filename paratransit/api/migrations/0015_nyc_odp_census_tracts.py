# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 21:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_nyct_subway_stops'),
    ]

    operations = [
        migrations.CreateModel(
            name='nyc_odp_census_tracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntacode', models.CharField(max_length=254)),
                ('ctlabel', models.CharField(max_length=254)),
                ('cdeligibil', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('ntaname', models.CharField(max_length=254)),
                ('boro_name', models.CharField(max_length=254)),
                ('boro_ct201', models.CharField(max_length=254)),
                ('shape_area', models.FloatField()),
                ('boro_code', models.CharField(max_length=254)),
                ('ct2010', models.CharField(max_length=254)),
                ('puma', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
