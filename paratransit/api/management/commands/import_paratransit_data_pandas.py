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

			#date and time fields
			df['tripdate'] = pd.to_datetime(df['tripdate'])

			df['picktime'] = pd.to_datetime(df['picktime'], errors='coerce')
			if df['picktime'] == 'NaT':
				df['picktime'] = None

			df['droptime'] = pd.to_datetime(df['droptime'])
			if df['droptime'] == 'NaT':
				df['droptime'] = None

			df['pickdate'] = pd.to_datetime(df['pickdate'])
			df['dropdate'] = pd.to_datetime(df['dropdate'])

			#boolean fields
			if df['shared'] == 1:
				df['shared'] = True
			else:
				df['shared'] = False

			if df['p_val'] == 1:
				df['p_val'] = True
			else:
				df['p_val'] = False

			if df['d_val'] == 1:
				df['d_val'] = True
			else:
				df['d_val'] = False

			if df['osrm_rval'] == 1:
				df['osrm_rval'] = True
			else:
				df['osrm_rval'] = False
			
			df.to_sql('api_trips', con=engine, if_exists='append')

			j+=1
			print '{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize)


	def handle(self, *args, **options):
		print "Truncate Table...."
		self.truncate_table()
		print "Load Paratransit Data with Pandas..."
		self.load_paratransit_data()




