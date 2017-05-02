import sys,os
from django.core.management.base import BaseCommand, CommandError
from api.models import *
import csv
from django.db import connection
from django.conf import settings

import pandas as pd
from sqlalchemy import create_engine
import datetime as dt

#db connection
user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)



"""
  Loads parastransit data from CSV to postgres directory using pandas
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

	def truncate_table(self):
		cursor = connection.cursor()
		cursor.execute("TRUNCATE TABLE api_trips RESTART IDENTITY;")
	
	def load_paratransit_data(self):
		# load variables
		start = dt.datetime.now()
		chunksize = 1000
		j = 0
		index_start = 1

		# location of file
		filename = os.path.join('/mnt/volume-nyc1-01/paratransit_raw_data/', 'paratransit_2015_vars.csv')

		for df in pd.read_csv(filename, chunksize=chunksize, iterator=True, encoding='utf-8'):

			df.columns = df.columns.astype(str)

			for i, row in enumerate(df.values):

				# create date and time objects
				if row[3]:
					try:
						row[3] = datetime.datetime.strptime(row[3], "%Y-%m-%d").date()
					except Exception as e:
						row[3] = None
				else:
					row[3] = None

				if row[4]:
					try:
						row[4] = datetime.datetime.strptime(row[4], "%H:%M").time()
					except Exception as e:
						row[4] = None
				else:
					row[4] = None

				if row[5]:
					try:
						row[5] = datetime.datetime.strptime(row[5], "%H:%M").time()
					except Exception as e:
						row[5] = None						
				else:
					row[5] = None


				if row[19]:				
					row[19] = self.CheckInt(row[19])
					if row[19] == 1:
						row[19] = True
					else:
						row[19] = False
				else:
					row[19] = False

				# create date and time objects
				if row[30]:
					try:
						row[30] = datetime.datetime.strptime(row[30], "%Y-%m-%d").date()
					except Exception as e:
						row[30] = None						
				else:
					pickdate = None

				if row[31]:
					try:
						row[31] = datetime.datetime.strptime(row[31], "%Y-%m-%d").date()
					except Exception as e:
						row[31] = None						
				else:
					row[31] = None

				# boolean field
				if row[43]:				
					row[43] = self.CheckInt(row[43])
					if row[43] == 1:
						row[43] = True
					else:
						row[43] = False
				else:
					row[43] = False

				if row[48]:
					row[48] = self.CheckInt(row[48])
					if row[48] == 1:
						row[48] = True
					else:
						row[48] = False
				else:
					row[48] = False

				if row[62]:
					row[62] = self.CheckInt(row[62])
					if row[62] == 1:
						row[62] = True
					else:
						row[62] = False
				else:
					row[62] = False


			# #date and time fields
			# df['tripdate'] = pd.to_datetime(df['tripdate'])
			# try:
			# 	df['picktime'] = pd.to_datetime(df['picktime'])
			# except Exception as e:
			# 	df['picktime'] = None

			# try:
			# 	df['droptime'] = pd.to_datetime(df['droptime'])
			# except Exception as e:
			# 	df['droptime'] = None

			# df['pickdate'] = pd.to_datetime(df['pickdate'])
			# df['dropdate'] = pd.to_datetime(df['dropdate'])

			# #boolean fields
			# if df['shared'] == 1:
			# 	df['shared'] = True
			# else:
			# 	df['shared'] = False

			# if df['p_val']:				
			# 	df['p_val'] = self.CheckInt(df['p_val'])
			# 	if df['p_val'] == 1:
			# 		df['p_val'] = True
			# 	else:
			# 		df['p_val'] = False
			# else:
			# 	df['p_val'] = False

			# if df['d_val']:
			# 	df['d_val'] = self.CheckInt(df['d_val'])
			# 	if df['d_val'] == 1:
			# 		df['d_val'] = True
			# 	else:
			# 		df['d_val'] = False
			# else:
			# 	df['d_val'] = False

			# if df['osrm_rval']:
			# 	df['osrm_rval'] = self.CheckInt(df['osrm_rval'])
			# 	if df['osrm_rval'] == 1:
			# 		df['osrm_rval'] = True
			# 	else:
			# 		df['osrm_rval'] = False
			# else:
			# 	df['osrm_rval'] = False			
			
			df.to_sql('api_trips', con=engine, if_exists='append')

			j+=1
			print '{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize)


	def handle(self, *args, **options):
		print "Truncate Table...."
		self.truncate_table()
		print "Load Paratransit Data with Pandas..."
		self.load_paratransit_data()




