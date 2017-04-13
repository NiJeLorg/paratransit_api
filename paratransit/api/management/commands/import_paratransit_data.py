import sys,os
from django.core.management.base import BaseCommand, CommandError
from api.models import *
import csv
import datetime


"""
  Loads CHI hoods from CSV
"""
class Command(BaseCommand):

	def CheckInt(self, s):
		try: 
			int(float(s))
			return int(float(s))
		except ValueError:
			return None

	def CheckFloat(self, s):
		try: 
			float(s)
			return float(s)
		except ValueError:
			return None
	
	def load_paratransit_data(self):
		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		# open LIS_Beacon_Beach_WQdata.csv and dump into BeachWQSamples table
		with open(os.path.join(__location__, 'paratransit_2015_vars.csv'), 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if row[0] != 'miscidx': # Ignore the header row, import everything else
					print row[0]

					# create date and time objects
					if row[3]:
						tripdate = datetime.datetime.strptime(row[3], "%Y-%m-%d").date()
					else:
						tripdate = None

					if row[4]:
						picktime = datetime.datetime.strptime(row[4], "%H:%M").time()
					else:
						picktime = None

					if row[5]:
						droptime = datetime.datetime.strptime(row[5], "%H:%M").time()
					else:
						droptime = None

					# boolean field
					if row[19] == '1':
						shared = True
					else:
						shared = False


					# create date and time objects
					if row[30]:
						pickdate = datetime.datetime.strptime(row[30], "%Y-%m-%d").date()
					else:
						pickdate = None

					if row[31]:
						dropdate = datetime.datetime.strptime(row[31], "%Y-%m-%d").date()
					else:
						dropdate = None

					# boolean field
					if row[43]:				
						row[43] = self.CheckInt(row[43])
						if row[43] == 1:
							p_val = True
						else:
							p_val = False
					else:
						p_val = False

					if row[48]:
						row[48] = self.CheckInt(row[48])
						if row[48] == 1:
							d_val = True
						else:
							d_val = False
					else:
						d_val = False

					if row[62]:
						row[62] = self.CheckInt(row[62])
						if row[62] == 1:
							osrm_rval = True
						else:
							osrm_rval = False
					else:
						osrm_rval = False



					i = trips()

					i.miscidx = self.CheckInt(row[0])
					i.index = self.CheckInt(row[1])
					i.tripid = self.CheckInt(row[2])
					i.tripdate = tripdate
					i.picktime = picktime
					i.droptime = droptime
					i.provider = row[6]
					i.status = row[7]
					i.routeid = self.CheckInt(row[8])
					i.pickhousenumber = self.CheckInt(row[9])
					i.pickaddress1 = row[10]
					i.pickcity = row[11]
					i.pickcounty = row[12]
					i.pickzip = self.CheckInt(row[13])
					i.drophousenumber = self.CheckInt(row[14])
					i.dropaddress1 = row[15]
					i.dropcity = row[16]
					i.dropcounty = row[17]
					i.dropzip = self.CheckInt(row[18])
					i.shared = shared
					i.puzip = self.CheckInt(row[20])
					i.dozip = self.CheckInt(row[21])
					i.uid = self.CheckInt(row[22])
					i.puid = row[23]
					i.duid = row[24]
					i.count = self.CheckInt(row[25])
					i.pickboro = self.CheckInt(row[26])
					i.dropboro = self.CheckInt(row[27])
					i.upast = row[28]
					i.udast = row[29]
					i.pickdate = pickdate
					i.dropdate = dropdate
					i.pickhour = self.CheckInt(row[32])
					i.pickmin = self.CheckInt(row[33])
					i.drophour = self.CheckInt(row[34])
					i.dropmin = self.CheckInt(row[35])
					i.pickdaymins = self.CheckInt(row[36])
					i.dropdaymins = self.CheckInt(row[37])
					i.tripminsdelta = self.CheckInt(row[38])
					i.p_bctcb2010 = self.CheckInt(row[39])
					i.p_lat = self.CheckFloat(row[40])
					i.p_lon = self.CheckFloat(row[41])
					i.p_count = self.CheckInt(row[42])
					i.p_val = p_val
					i.d_bctcb2010 = self.CheckInt(row[44])
					i.d_lat = self.CheckFloat(row[45])
					i.d_lon = self.CheckFloat(row[46])
					i.d_count = self.CheckInt(row[47])
					i.d_val = d_val
					i.p_geoid = row[49]
					i.p_xcoord = self.CheckFloat(row[50])
					i.p_ycoord = self.CheckFloat(row[51])
					i.d_geoid = row[52]
					i.d_xcoord = self.CheckFloat(row[53])
					i.d_ycoord = self.CheckFloat(row[54])
					i.p_geoid_bg = row[55]
					i.d_geoid_bg = row[56]
					i.p_geoid_tr = row[57]
					i.d_geoid_tr = row[58]
					i.geoid_pair = row[59]
					i.osrmminsdelta = self.CheckFloat(row[60])
					i.osrm_dist = self.CheckFloat(row[61])
					i.osrm_rval = osrm_rval
					i.p_nr_bus = self.CheckFloat(row[63])
					i.p_nr_sub = self.CheckFloat(row[64])
					i.p_nr_hea = self.CheckFloat(row[65])
					i.d_nr_bus = self.CheckFloat(row[66])
					i.d_nr_sub = self.CheckFloat(row[67])
					i.d_nr_hea = self.CheckFloat(row[68])

					i.p_p_count = self.CheckInt(row[69])
					i.p_d_count = self.CheckInt(row[70])
					i.p_a_count = self.CheckInt(row[71])
					i.p_p0010001 = self.CheckInt(row[72])
					i.p_p0030001 = self.CheckInt(row[73])
					i.p_p0030002 = self.CheckInt(row[74])
					i.p_p0030003 = self.CheckInt(row[75])
					i.p_p0030004 = self.CheckInt(row[76])
					i.p_p0030005 = self.CheckInt(row[77])
					i.p_p0030006 = self.CheckInt(row[78])
					i.p_p0030007 = self.CheckInt(row[79])
					i.p_p0030008 = self.CheckInt(row[80])
					i.p_p0040001 = self.CheckInt(row[81])
					i.p_p0040002 = self.CheckInt(row[82])
					i.p_p0040003 = self.CheckInt(row[83])
					i.p_p0120001 = self.CheckInt(row[84])
					i.p_p0120002 = self.CheckInt(row[85])
					i.p_p0120003 = self.CheckInt(row[86])
					i.p_p0120004 = self.CheckInt(row[87])
					i.p_p0120005 = self.CheckInt(row[88])
					i.p_p0120006 = self.CheckInt(row[89])
					i.p_p0120007 = self.CheckInt(row[90])
					i.p_p0120008 = self.CheckInt(row[91])
					i.p_p0120009 = self.CheckInt(row[92])
					i.p_p0120010 = self.CheckInt(row[93])
					i.p_p0120011 = self.CheckInt(row[94])
					i.p_p0120012 = self.CheckInt(row[95])
					i.p_p0120013 = self.CheckInt(row[96])
					i.p_p0120014 = self.CheckInt(row[97])
					i.p_p0120015 = self.CheckInt(row[98])
					i.p_p0120016 = self.CheckInt(row[99])
					i.p_p0120017 = self.CheckInt(row[100])
					i.p_p0120018 = self.CheckInt(row[101])
					i.p_p0120019 = self.CheckInt(row[102])
					i.p_p0120020 = self.CheckInt(row[103])
					i.p_p0120021 = self.CheckInt(row[104])
					i.p_p0120022 = self.CheckInt(row[105])
					i.p_p0120023 = self.CheckInt(row[106])
					i.p_p0120024 = self.CheckInt(row[107])
					i.p_p0120025 = self.CheckInt(row[108])
					i.p_p0120026 = self.CheckInt(row[109])
					i.p_p0120027 = self.CheckInt(row[110])
					i.p_p0120028 = self.CheckInt(row[111])
					i.p_p0120029 = self.CheckInt(row[112])
					i.p_p0120030 = self.CheckInt(row[113])
					i.p_p0120031 = self.CheckInt(row[114])
					i.p_p0120032 = self.CheckInt(row[115])
					i.p_p0120033 = self.CheckInt(row[116])
					i.p_p0120034 = self.CheckInt(row[117])
					i.p_p0120035 = self.CheckInt(row[118])
					i.p_p0120036 = self.CheckInt(row[119])
					i.p_p0120037 = self.CheckInt(row[120])
					i.p_p0120038 = self.CheckInt(row[121])
					i.p_p0120039 = self.CheckInt(row[122])
					i.p_p0120040 = self.CheckInt(row[123])
					i.p_p0120041 = self.CheckInt(row[124])
					i.p_p0120042 = self.CheckInt(row[125])
					i.p_p0120043 = self.CheckInt(row[126])
					i.p_p0120044 = self.CheckInt(row[127])
					i.p_p0120045 = self.CheckInt(row[128])
					i.p_p0120046 = self.CheckInt(row[129])
					i.p_p0120047 = self.CheckInt(row[130])
					i.p_p0120048 = self.CheckInt(row[131])
					i.p_p0120049 = self.CheckInt(row[132])
					i.p_h00010001 = self.CheckInt(row[133])
					i.p_h0030001 = self.CheckInt(row[134])
					i.p_h0030002 = self.CheckInt(row[135])
					i.p_h0030003 = self.CheckInt(row[136])
					i.p_h0040001 = self.CheckInt(row[137])
					i.p_h0040002 = self.CheckInt(row[138])
					i.p_h0040003 = self.CheckInt(row[139])
					i.p_h0040004 = self.CheckInt(row[140])
					i.p_h0050001 = self.CheckInt(row[141])
					i.p_h0050002 = self.CheckInt(row[142])
					i.p_h0050003 = self.CheckInt(row[143])
					i.p_h0050004 = self.CheckInt(row[144])
					i.p_h0050005 = self.CheckInt(row[145])
					i.p_h0050006 = self.CheckInt(row[146])
					i.p_h0050007 = self.CheckInt(row[147])
					i.p_h0050008 = self.CheckInt(row[148])
					i.p_p_pop = self.CheckFloat(row[149])
					i.p_d_pop = self.CheckFloat(row[150])
					i.p_a_pop = self.CheckFloat(row[151])
					i.d_p_count = self.CheckInt(row[152])
					i.d_d_count = self.CheckInt(row[153])
					i.d_a_count = self.CheckInt(row[154])
					i.d_p0010001 = self.CheckInt(row[155])
					i.d_p0030001 = self.CheckInt(row[156])
					i.d_p0030002 = self.CheckInt(row[157])
					i.d_p0030003 = self.CheckInt(row[158])
					i.d_p0030004 = self.CheckInt(row[159])
					i.d_p0030005 = self.CheckInt(row[160])
					i.d_p0030006 = self.CheckInt(row[161])
					i.d_p0030007 = self.CheckInt(row[162])
					i.d_p0030008 = self.CheckInt(row[163])
					i.d_p0040001 = self.CheckInt(row[164])
					i.d_p0040002 = self.CheckInt(row[165])
					i.d_p0040003 = self.CheckInt(row[166])
					i.d_p0120001 = self.CheckInt(row[167])
					i.d_p0120002 = self.CheckInt(row[168])
					i.d_p0120003 = self.CheckInt(row[169])
					i.d_p0120004 = self.CheckInt(row[170])
					i.d_p0120005 = self.CheckInt(row[171])
					i.d_p0120006 = self.CheckInt(row[172])
					i.d_p0120007 = self.CheckInt(row[173])
					i.d_p0120008 = self.CheckInt(row[174])
					i.d_p0120009 = self.CheckInt(row[175])
					i.d_p0120010 = self.CheckInt(row[176])
					i.d_p0120011 = self.CheckInt(row[177])
					i.d_p0120012 = self.CheckInt(row[178])
					i.d_p0120013 = self.CheckInt(row[179])
					i.d_p0120014 = self.CheckInt(row[180])
					i.d_p0120015 = self.CheckInt(row[181])
					i.d_p0120016 = self.CheckInt(row[182])
					i.d_p0120017 = self.CheckInt(row[183])
					i.d_p0120018 = self.CheckInt(row[184])
					i.d_p0120019 = self.CheckInt(row[185])
					i.d_p0120020 = self.CheckInt(row[186])
					i.d_p0120021 = self.CheckInt(row[187])
					i.d_p0120022 = self.CheckInt(row[188])
					i.d_p0120023 = self.CheckInt(row[189])
					i.d_p0120024 = self.CheckInt(row[190])
					i.d_p0120025 = self.CheckInt(row[191])
					i.d_p0120026 = self.CheckInt(row[192])
					i.d_p0120027 = self.CheckInt(row[193])
					i.d_p0120028 = self.CheckInt(row[194])
					i.d_p0120029 = self.CheckInt(row[195])
					i.d_p0120030 = self.CheckInt(row[196])
					i.d_p0120031 = self.CheckInt(row[197])
					i.d_p0120032 = self.CheckInt(row[198])
					i.d_p0120033 = self.CheckInt(row[199])
					i.d_p0120034 = self.CheckInt(row[200])
					i.d_p0120035 = self.CheckInt(row[201])
					i.d_p0120036 = self.CheckInt(row[202])
					i.d_p0120037 = self.CheckInt(row[203])
					i.d_p0120038 = self.CheckInt(row[204])
					i.d_p0120039 = self.CheckInt(row[205])
					i.d_p0120040 = self.CheckInt(row[206])
					i.d_p0120041 = self.CheckInt(row[207])
					i.d_p0120042 = self.CheckInt(row[208])
					i.d_p0120043 = self.CheckInt(row[209])
					i.d_p0120044 = self.CheckInt(row[210])
					i.d_p0120045 = self.CheckInt(row[211])
					i.d_p0120046 = self.CheckInt(row[212])
					i.d_p0120047 = self.CheckInt(row[213])
					i.d_p0120048 = self.CheckInt(row[214])
					i.d_p0120049 = self.CheckInt(row[215])
					i.d_h00010001 = self.CheckInt(row[216])
					i.d_h0030001 = self.CheckInt(row[217])
					i.d_h0030002 = self.CheckInt(row[218])
					i.d_h0030003 = self.CheckInt(row[219])
					i.d_h0040001 = self.CheckInt(row[220])
					i.d_h0040002 = self.CheckInt(row[221])
					i.d_h0040003 = self.CheckInt(row[222])
					i.d_h0040004 = self.CheckInt(row[223])
					i.d_h0050001 = self.CheckInt(row[224])
					i.d_h0050002 = self.CheckInt(row[225])
					i.d_h0050003 = self.CheckInt(row[226])
					i.d_h0050004 = self.CheckInt(row[227])
					i.d_h0050005 = self.CheckInt(row[228])
					i.d_h0050006 = self.CheckInt(row[229])
					i.d_h0050007 = self.CheckInt(row[230])
					i.d_h0050008 = self.CheckInt(row[231])
					i.d_p_pop = self.CheckFloat(row[232])
					i.d_d_pop = self.CheckFloat(row[233])
					i.d_a_pop = self.CheckFloat(row[234])
					i.p_b01001_001e_x = self.CheckInt(row[235])
					i.p_b01001_002e_x = self.CheckInt(row[236])
					i.p_b01001_003e_x = self.CheckInt(row[237])
					i.p_b01001_004e_x = self.CheckInt(row[238])
					i.p_b01001_005e_x = self.CheckInt(row[239])
					i.p_b01001_006e_x = self.CheckInt(row[240])
					i.p_b01001_007e_x = self.CheckInt(row[241])
					i.p_b01001_008e_x = self.CheckInt(row[242])
					i.p_b01001_009e_x = self.CheckInt(row[243])
					i.p_b01001_010e_x = self.CheckInt(row[244])
					i.p_b01001_011e_x = self.CheckInt(row[245])
					i.p_b01001_012e_x = self.CheckInt(row[246])
					i.p_b01001_013e_x = self.CheckInt(row[247])
					i.p_b01001_014e_x = self.CheckInt(row[248])
					i.p_b01001_015e_x = self.CheckInt(row[249])
					i.p_b01001_016e_x = self.CheckInt(row[250])
					i.p_b01001_017e_x = self.CheckInt(row[251])
					i.p_b01001_018e_x = self.CheckInt(row[252])
					i.p_b01001_019e_x = self.CheckInt(row[253])
					i.p_b01001_020e_x = self.CheckInt(row[254])
					i.p_b01001_021e_x = self.CheckInt(row[255])
					i.p_b01001_022e_x = self.CheckInt(row[256])
					i.p_b01001_023e_x = self.CheckInt(row[257])
					i.p_b01001_024e_x = self.CheckInt(row[258])
					i.p_b01001_025e_x = self.CheckInt(row[259])
					i.p_b01001_026e_x = self.CheckInt(row[260])
					i.p_b01001_027e_x = self.CheckInt(row[261])
					i.p_b01001_028e_x = self.CheckInt(row[262])
					i.p_b01001_029e_x = self.CheckInt(row[263])
					i.p_b01001_030e_x = self.CheckInt(row[264])
					i.p_b01001_031e_x = self.CheckInt(row[265])
					i.p_b01001_032e_x = self.CheckInt(row[266])
					i.p_b01001_033e_x = self.CheckInt(row[267])
					i.p_b01001_034e_x = self.CheckInt(row[268])
					i.p_b01001_035e_x = self.CheckInt(row[269])
					i.p_b01001_036e_x = self.CheckInt(row[270])
					i.p_b01001_037e_x = self.CheckInt(row[271])
					i.p_b01001_038e_x = self.CheckInt(row[272])
					i.p_b01001_039e_x = self.CheckInt(row[273])
					i.p_b01001_040e_x = self.CheckInt(row[274])
					i.p_b01001_041e_x = self.CheckInt(row[275])
					i.p_b01001_042e_x = self.CheckInt(row[276])
					i.p_b01001_043e_x = self.CheckInt(row[277])
					i.p_b01001_044e_x = self.CheckInt(row[278])
					i.p_b01001_045e_x = self.CheckInt(row[279])
					i.p_b01001_046e_x = self.CheckInt(row[280])
					i.p_b01001_047e_x = self.CheckInt(row[281])
					i.p_b01001_048e_x = self.CheckInt(row[282])
					i.p_b01001_049e_x = self.CheckInt(row[283])
					i.p_b01003_001e_x = self.CheckInt(row[284])
					i.p_b19013_001e_x = self.CheckInt(row[285])
					i.p_b18101_001e_x = self.CheckInt(row[286])
					i.d_b01001_001e_x = self.CheckInt(row[287])
					i.d_b01001_002e_x = self.CheckInt(row[288])
					i.d_b01001_003e_x = self.CheckInt(row[289])
					i.d_b01001_004e_x = self.CheckInt(row[290])
					i.d_b01001_005e_x = self.CheckInt(row[291])
					i.d_b01001_006e_x = self.CheckInt(row[292])
					i.d_b01001_007e_x = self.CheckInt(row[293])
					i.d_b01001_008e_x = self.CheckInt(row[294])
					i.d_b01001_009e_x = self.CheckInt(row[295])
					i.d_b01001_010e_x = self.CheckInt(row[296])
					i.d_b01001_011e_x = self.CheckInt(row[297])
					i.d_b01001_012e_x = self.CheckInt(row[298])
					i.d_b01001_013e_x = self.CheckInt(row[299])
					i.d_b01001_014e_x = self.CheckInt(row[300])
					i.d_b01001_015e_x = self.CheckInt(row[301])
					i.d_b01001_016e_x = self.CheckInt(row[302])
					i.d_b01001_017e_x = self.CheckInt(row[303])
					i.d_b01001_018e_x = self.CheckInt(row[304])
					i.d_b01001_019e_x = self.CheckInt(row[305])
					i.d_b01001_020e_x = self.CheckInt(row[306])
					i.d_b01001_021e_x = self.CheckInt(row[307])
					i.d_b01001_022e_x = self.CheckInt(row[308])
					i.d_b01001_023e_x = self.CheckInt(row[309])
					i.d_b01001_024e_x = self.CheckInt(row[310])
					i.d_b01001_025e_x = self.CheckInt(row[311])
					i.d_b01001_026e_x = self.CheckInt(row[312])
					i.d_b01001_027e_x = self.CheckInt(row[313])
					i.d_b01001_028e_x = self.CheckInt(row[314])
					i.d_b01001_029e_x = self.CheckInt(row[315])
					i.d_b01001_030e_x = self.CheckInt(row[316])
					i.d_b01001_031e_x = self.CheckInt(row[317])
					i.d_b01001_032e_x = self.CheckInt(row[318])
					i.d_b01001_033e_x = self.CheckInt(row[319])
					i.d_b01001_034e_x = self.CheckInt(row[320])
					i.d_b01001_035e_x = self.CheckInt(row[321])
					i.d_b01001_036e_x = self.CheckInt(row[322])
					i.d_b01001_037e_x = self.CheckInt(row[323])
					i.d_b01001_038e_x = self.CheckInt(row[324])
					i.d_b01001_039e_x = self.CheckInt(row[325])
					i.d_b01001_040e_x = self.CheckInt(row[326])
					i.d_b01001_041e_x = self.CheckInt(row[327])
					i.d_b01001_042e_x = self.CheckInt(row[328])
					i.d_b01001_043e_x = self.CheckInt(row[329])
					i.d_b01001_044e_x = self.CheckInt(row[330])
					i.d_b01001_045e_x = self.CheckInt(row[331])
					i.d_b01001_046e_x = self.CheckInt(row[332])
					i.d_b01001_047e_x = self.CheckInt(row[333])
					i.d_b01001_048e_x = self.CheckInt(row[334])
					i.d_b01001_049e_x = self.CheckInt(row[335])
					i.d_b01003_001e_x = self.CheckInt(row[336])
					i.d_b19013_001e_x = self.CheckInt(row[337])
					i.d_b18101_001e_x = self.CheckInt(row[338]) 
					i.p_b01001_001e_y = self.CheckInt(row[339])
					i.p_b01001_002e_y = self.CheckInt(row[340])
					i.p_b01001_003e_y = self.CheckInt(row[341])
					i.p_b01001_004e_y = self.CheckInt(row[342])
					i.p_b01001_005e_y = self.CheckInt(row[343])
					i.p_b01001_006e_y = self.CheckInt(row[344])
					i.p_b01001_007e_y = self.CheckInt(row[345])
					i.p_b01001_008e_y = self.CheckInt(row[346])
					i.p_b01001_009e_y = self.CheckInt(row[347])
					i.p_b01001_010e_y = self.CheckInt(row[348])
					i.p_b01001_011e_y = self.CheckInt(row[349])
					i.p_b01001_012e_y = self.CheckInt(row[350])
					i.p_b01001_013e_y = self.CheckInt(row[351])
					i.p_b01001_014e_y = self.CheckInt(row[352])
					i.p_b01001_015e_y = self.CheckInt(row[353])
					i.p_b01001_016e_y = self.CheckInt(row[354])
					i.p_b01001_017e_y = self.CheckInt(row[355])
					i.p_b01001_018e_y = self.CheckInt(row[356])
					i.p_b01001_019e_y = self.CheckInt(row[357])
					i.p_b01001_020e_y = self.CheckInt(row[358])
					i.p_b01001_021e_y = self.CheckInt(row[359])
					i.p_b01001_022e_y = self.CheckInt(row[360])
					i.p_b01001_023e_y = self.CheckInt(row[361])
					i.p_b01001_024e_y = self.CheckInt(row[362])
					i.p_b01001_025e_y = self.CheckInt(row[363])
					i.p_b01001_026e_y = self.CheckInt(row[364])
					i.p_b01001_027e_y = self.CheckInt(row[365])
					i.p_b01001_028e_y = self.CheckInt(row[366])
					i.p_b01001_029e_y = self.CheckInt(row[367])
					i.p_b01001_030e_y = self.CheckInt(row[368])
					i.p_b01001_031e_y = self.CheckInt(row[369])
					i.p_b01001_032e_y = self.CheckInt(row[370])
					i.p_b01001_033e_y = self.CheckInt(row[371])
					i.p_b01001_034e_y = self.CheckInt(row[372])
					i.p_b01001_035e_y = self.CheckInt(row[373])
					i.p_b01001_036e_y = self.CheckInt(row[374])
					i.p_b01001_037e_y = self.CheckInt(row[375])
					i.p_b01001_038e_y = self.CheckInt(row[376])
					i.p_b01001_039e_y = self.CheckInt(row[377])
					i.p_b01001_040e_y = self.CheckInt(row[378])
					i.p_b01001_041e_y = self.CheckInt(row[379])
					i.p_b01001_042e_y = self.CheckInt(row[380])
					i.p_b01001_043e_y = self.CheckInt(row[381])
					i.p_b01001_044e_y = self.CheckInt(row[382])
					i.p_b01001_045e_y = self.CheckInt(row[383])
					i.p_b01001_046e_y = self.CheckInt(row[384])
					i.p_b01001_047e_y = self.CheckInt(row[385])
					i.p_b01001_048e_y = self.CheckInt(row[386])
					i.p_b01001_049e_y = self.CheckInt(row[387])
					i.p_b01003_001e_y = self.CheckInt(row[388])
					i.p_b19013_001e_y = self.CheckInt(row[389])
					i.p_b18101_001e_y = self.CheckInt(row[390])
					i.d_b01001_001e_y = self.CheckInt(row[391])
					i.d_b01001_002e_y = self.CheckInt(row[392])
					i.d_b01001_003e_y = self.CheckInt(row[393])
					i.d_b01001_004e_y = self.CheckInt(row[394])
					i.d_b01001_005e_y = self.CheckInt(row[395])
					i.d_b01001_006e_y = self.CheckInt(row[396])
					i.d_b01001_007e_y = self.CheckInt(row[397])
					i.d_b01001_008e_y = self.CheckInt(row[398])
					i.d_b01001_009e_y = self.CheckInt(row[399])
					i.d_b01001_010e_y = self.CheckInt(row[400])
					i.d_b01001_011e_y = self.CheckInt(row[401])
					i.d_b01001_012e_y = self.CheckInt(row[402])
					i.d_b01001_013e_y = self.CheckInt(row[403])
					i.d_b01001_014e_y = self.CheckInt(row[404])
					i.d_b01001_015e_y = self.CheckInt(row[405])
					i.d_b01001_016e_y = self.CheckInt(row[406])
					i.d_b01001_017e_y = self.CheckInt(row[407])
					i.d_b01001_018e_y = self.CheckInt(row[408])
					i.d_b01001_019e_y = self.CheckInt(row[409])
					i.d_b01001_020e_y = self.CheckInt(row[410])
					i.d_b01001_021e_y = self.CheckInt(row[411])
					i.d_b01001_022e_y = self.CheckInt(row[412])
					i.d_b01001_023e_y = self.CheckInt(row[413])
					i.d_b01001_024e_y = self.CheckInt(row[414])
					i.d_b01001_025e_y = self.CheckInt(row[415])
					i.d_b01001_026e_y = self.CheckInt(row[416])
					i.d_b01001_027e_y = self.CheckInt(row[417])
					i.d_b01001_028e_y = self.CheckInt(row[419])
					i.d_b01001_029e_y = self.CheckInt(row[419])
					i.d_b01001_030e_y = self.CheckInt(row[420])
					i.d_b01001_031e_y = self.CheckInt(row[421])
					i.d_b01001_032e_y = self.CheckInt(row[422])
					i.d_b01001_033e_y = self.CheckInt(row[423])
					i.d_b01001_034e_y = self.CheckInt(row[424])
					i.d_b01001_035e_y = self.CheckInt(row[425])
					i.d_b01001_036e_y = self.CheckInt(row[426])
					i.d_b01001_037e_y = self.CheckInt(row[427])
					i.d_b01001_038e_y = self.CheckInt(row[428])
					i.d_b01001_039e_y = self.CheckInt(row[429])
					i.d_b01001_040e_y = self.CheckInt(row[430])
					i.d_b01001_041e_y = self.CheckInt(row[431])
					i.d_b01001_042e_y = self.CheckInt(row[432])
					i.d_b01001_043e_y = self.CheckInt(row[433])
					i.d_b01001_044e_y = self.CheckInt(row[434])
					i.d_b01001_045e_y = self.CheckInt(row[435])
					i.d_b01001_046e_y = self.CheckInt(row[436])
					i.d_b01001_047e_y = self.CheckInt(row[437])
					i.d_b01001_048e_y = self.CheckInt(row[438])
					i.d_b01001_049e_y = self.CheckInt(row[439])
					i.d_b01003_001e_y = self.CheckInt(row[440])
					i.d_b19013_001e_y = self.CheckInt(row[441])
					i.d_b18101_001e_y = self.CheckInt(row[442]) 

					i.save()

	def handle(self, *args, **options):
		print "Load Paratransit Data..."
		self.load_paratransit_data()




