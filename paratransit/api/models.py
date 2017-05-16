# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


# trips model
class trips(models.Model):
	level_0 = models.IntegerField(default=0, null=True, blank=True)
	miscidx = models.IntegerField(default=0, null=True, blank=True)
	index = models.IntegerField(default=0, null=True, blank=True)
	tripid = models.BigIntegerField(default=0, null=True, blank=True)
	tripdate = models.DateField(default=None, null=True, blank=True)
	picktime = models.TimeField(default=None, null=True, blank=True)
	droptime = models.TimeField(default=None, null=True, blank=True)
	provider = models.CharField(max_length=255, null=True, blank=True)
	status = models.CharField(max_length=255, null=True, blank=True)
	routeid = models.IntegerField(default=0, null=True, blank=True)
	pickhousenumber = models.CharField(max_length=255, null=True, blank=True)
	pickaddress1 = models.CharField(max_length=255, null=True, blank=True)
	pickcity = models.CharField(max_length=255, null=True, blank=True)
	pickcounty = models.CharField(max_length=255, null=True, blank=True)
	pickzip = models.CharField(max_length=255, null=True, blank=True)
	drophousenumber = models.CharField(max_length=255, null=True, blank=True)
	dropaddress1 = models.CharField(max_length=255, null=True, blank=True)
	dropcity = models.CharField(max_length=255, null=True, blank=True)
	dropcounty = models.CharField(max_length=255, null=True, blank=True)
	dropzip = models.CharField(max_length=255, null=True, blank=True)
	shared = models.BooleanField(default=False, blank=True)
	puzip = models.CharField(max_length=255, null=True, blank=True)
	dozip = models.CharField(max_length=255, null=True, blank=True)
	uid = models.IntegerField(default=0, null=True, blank=True)
	puid = models.CharField(max_length=255, null=True, blank=True)
	duid = models.CharField(max_length=255, null=True, blank=True)
	count = models.IntegerField(default=0, null=True, blank=True)
	pickboro = models.IntegerField(default=0, null=True, blank=True)
	dropboro = models.IntegerField(default=0, null=True, blank=True)
	upast = models.CharField(max_length=255, null=True, blank=True)
	udast = models.CharField(max_length=255, null=True, blank=True)
	pickdate = models.DateField(default=None, null=True, blank=True)
	dropdate = models.DateField(default=None, null=True, blank=True)
	pickhour = models.IntegerField(default=0, null=True, blank=True)
	pickmin = models.IntegerField(default=0, null=True, blank=True)
	drophour = models.IntegerField(default=0, null=True, blank=True)
	dropmin = models.IntegerField(default=0, null=True, blank=True)
	pickdaymins = models.IntegerField(default=0, null=True, blank=True)
	dropdaymins = models.IntegerField(default=0, null=True, blank=True)
	tripminsdelta = models.IntegerField(default=0, null=True, blank=True)
	p_bctcb2010 = models.BigIntegerField(default=0, null=True, blank=True)
	p_lat = models.FloatField(default=0, null=True, blank=True)
	p_lng = models.FloatField(default=0, null=True, blank=True)
	p_count = models.IntegerField(default=0, null=True, blank=True)
	p_val = models.BooleanField(default=False, blank=True)
	d_bctcb2010 = models.BigIntegerField(default=0, null=True, blank=True)
	d_lat = models.FloatField(default=0, null=True, blank=True)
	d_lng = models.FloatField(default=0, null=True, blank=True)
	d_count = models.IntegerField(default=0, null=True, blank=True)
	d_val = models.BooleanField(default=False, blank=True)
	p_geoid = models.CharField(max_length=255, null=True, blank=True)
	p_xcoord = models.FloatField(default=0, null=True, blank=True)
	p_ycoord = models.FloatField(default=0, null=True, blank=True)
	d_geoid = models.CharField(max_length=255, null=True, blank=True)
	d_xcoord = models.FloatField(default=0, null=True, blank=True)
	d_ycoord = models.FloatField(default=0, null=True, blank=True)
	p_geoid_bg = models.CharField(max_length=255, null=True, blank=True)
	d_geoid_bg = models.CharField(max_length=255, null=True, blank=True)
	p_geoid_tr = models.CharField(max_length=255, null=True, blank=True)
	d_geoid_tr = models.CharField(max_length=255, null=True, blank=True)
	geoid_pair = models.CharField(max_length=255, null=True, blank=True)
	osrmminsdelta = models.FloatField(default=0, null=True, blank=True)
	osrm_dist = models.FloatField(default=0, null=True, blank=True)
	osrm_rval = models.BooleanField(default=False, blank=True)
	p_nr_bus = models.FloatField(default=0, null=True, blank=True)
	d_nr_bus = models.FloatField(default=0, null=True, blank=True)
	p_nr_sub = models.FloatField(default=0, null=True, blank=True)
	d_nr_sub = models.FloatField(default=0, null=True, blank=True)
	p_nr_hea = models.FloatField(default=0, null=True, blank=True)
	d_nr_hea = models.FloatField(default=0, null=True, blank=True)
	p_p_count = models.IntegerField(default=0, null=True, blank=True)
	p_d_count = models.IntegerField(default=0, null=True, blank=True)
	p_a_count = models.IntegerField(default=0, null=True, blank=True)
	p_p0010001 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030001 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030002 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030003 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030004 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030005 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030006 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030007 = models.IntegerField(default=0, null=True, blank=True)
	p_p0030008 = models.IntegerField(default=0, null=True, blank=True)
	p_p0040001 = models.IntegerField(default=0, null=True, blank=True)
	p_p0040002 = models.IntegerField(default=0, null=True, blank=True)
	p_p0040003 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120001 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120002 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120003 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120004 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120005 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120006 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120007 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120008 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120009 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120010 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120011 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120012 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120013 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120014 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120015 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120016 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120017 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120018 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120019 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120020 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120021 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120022 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120023 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120024 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120025 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120026 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120027 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120028 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120029 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120030 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120031 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120032 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120033 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120034 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120035 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120036 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120037 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120038 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120039 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120040 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120041 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120042 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120043 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120044 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120045 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120046 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120047 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120048 = models.IntegerField(default=0, null=True, blank=True)
	p_p0120049 = models.IntegerField(default=0, null=True, blank=True)
	p_h00010001 = models.IntegerField(default=0, null=True, blank=True)
	p_h0030001 = models.IntegerField(default=0, null=True, blank=True)
	p_h0030002 = models.IntegerField(default=0, null=True, blank=True)
	p_h0030003 = models.IntegerField(default=0, null=True, blank=True)
	p_h0040001 = models.IntegerField(default=0, null=True, blank=True)
	p_h0040002 = models.IntegerField(default=0, null=True, blank=True)
	p_h0040003 = models.IntegerField(default=0, null=True, blank=True)
	p_h0040004 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050001 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050002 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050003 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050004 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050005 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050006 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050007 = models.IntegerField(default=0, null=True, blank=True)
	p_h0050008 = models.IntegerField(default=0, null=True, blank=True)
	p_p_pop = models.FloatField(default=0, null=True, blank=True)
	p_d_pop = models.FloatField(default=0, null=True, blank=True)
	p_a_pop = models.FloatField(default=0, null=True, blank=True)
	d_p_count = models.IntegerField(default=0, null=True, blank=True)
	d_d_count = models.IntegerField(default=0, null=True, blank=True)
	d_a_count = models.IntegerField(default=0, null=True, blank=True)
	d_p0010001 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030001 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030002 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030003 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030004 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030005 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030006 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030007 = models.IntegerField(default=0, null=True, blank=True)
	d_p0030008 = models.IntegerField(default=0, null=True, blank=True)
	d_p0040001 = models.IntegerField(default=0, null=True, blank=True)
	d_p0040002 = models.IntegerField(default=0, null=True, blank=True)
	d_p0040003 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120001 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120002 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120003 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120004 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120005 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120006 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120007 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120008 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120009 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120010 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120011 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120012 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120013 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120014 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120015 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120016 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120017 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120018 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120019 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120020 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120021 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120022 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120023 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120024 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120025 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120026 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120027 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120028 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120029 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120030 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120031 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120032 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120033 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120034 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120035 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120036 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120037 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120038 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120039 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120040 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120041 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120042 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120043 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120044 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120045 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120046 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120047 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120048 = models.IntegerField(default=0, null=True, blank=True)
	d_p0120049 = models.IntegerField(default=0, null=True, blank=True)
	d_h00010001 = models.IntegerField(default=0, null=True, blank=True)
	d_h0030001 = models.IntegerField(default=0, null=True, blank=True)
	d_h0030002 = models.IntegerField(default=0, null=True, blank=True)
	d_h0030003 = models.IntegerField(default=0, null=True, blank=True)
	d_h0040001 = models.IntegerField(default=0, null=True, blank=True)
	d_h0040002 = models.IntegerField(default=0, null=True, blank=True)
	d_h0040003 = models.IntegerField(default=0, null=True, blank=True)
	d_h0040004 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050001 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050002 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050003 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050004 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050005 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050006 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050007 = models.IntegerField(default=0, null=True, blank=True)
	d_h0050008 = models.IntegerField(default=0, null=True, blank=True)
	d_p_pop = models.FloatField(default=0, null=True, blank=True)
	d_d_pop = models.FloatField(default=0, null=True, blank=True)
	d_a_pop = models.FloatField(default=0, null=True, blank=True)
	p_b01001_001e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_002e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_003e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_004e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_005e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_006e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_007e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_008e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_009e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_010e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_011e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_012e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_013e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_014e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_015e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_016e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_017e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_018e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_019e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_020e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_021e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_022e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_023e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_024e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_025e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_026e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_027e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_028e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_029e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_030e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_031e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_032e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_033e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_034e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_035e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_036e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_037e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_038e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_039e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_040e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_041e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_042e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_043e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_044e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_045e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_046e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_047e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_048e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_049e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b01003_001e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b19013_001e_x = models.IntegerField(default=0, null=True, blank=True)
	p_b18101_001e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_001e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_002e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_003e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_004e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_005e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_006e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_007e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_008e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_009e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_010e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_011e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_012e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_013e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_014e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_015e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_016e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_017e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_018e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_019e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_020e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_021e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_022e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_023e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_024e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_025e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_026e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_027e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_028e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_029e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_030e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_031e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_032e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_033e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_034e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_035e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_036e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_037e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_038e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_039e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_040e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_041e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_042e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_043e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_044e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_045e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_046e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_047e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_048e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_049e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b01003_001e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b19013_001e_x = models.IntegerField(default=0, null=True, blank=True)
	d_b18101_001e_x = models.IntegerField(default=0, null=True, blank=True)	
	p_b01001_001e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_002e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_003e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_004e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_005e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_006e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_007e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_008e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_009e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_010e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_011e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_012e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_013e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_014e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_015e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_016e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_017e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_018e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_019e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_020e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_021e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_022e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_023e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_024e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_025e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_026e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_027e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_028e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_029e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_030e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_031e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_032e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_033e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_034e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_035e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_036e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_037e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_038e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_039e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_040e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_041e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_042e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_043e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_044e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_045e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_046e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_047e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_048e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01001_049e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b01003_001e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b19013_001e_y = models.IntegerField(default=0, null=True, blank=True)
	p_b18101_001e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_001e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_002e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_003e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_004e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_005e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_006e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_007e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_008e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_009e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_010e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_011e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_012e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_013e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_014e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_015e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_016e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_017e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_018e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_019e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_020e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_021e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_022e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_023e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_024e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_025e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_026e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_027e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_028e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_029e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_030e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_031e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_032e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_033e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_034e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_035e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_036e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_037e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_038e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_039e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_040e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_041e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_042e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_043e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_044e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_045e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_046e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_047e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_048e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01001_049e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b01003_001e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b19013_001e_y = models.IntegerField(default=0, null=True, blank=True)
	d_b18101_001e_y = models.IntegerField(default=0, null=True, blank=True)		

# pickups model
class pickup_locations(models.Model):
	trip = models.OneToOneField(trips, on_delete=models.CASCADE)
	tripid = models.BigIntegerField(default=0, null=True, blank=True)
	p_lat = models.FloatField(default=0, null=True, blank=True)
	p_lng = models.FloatField(default=0, null=True, blank=True)
	the_geom = models.PointField(null=True, blank=True)

# dropoffs model 
class dropoff_locations(models.Model):
	trip = models.OneToOneField(trips, on_delete=models.CASCADE)
	tripid = models.BigIntegerField(default=0, null=True, blank=True)
	d_lat = models.FloatField(default=0, null=True, blank=True)
	d_lng = models.FloatField(default=0, null=True, blank=True)
	the_geom = models.PointField(null=True, blank=True)




