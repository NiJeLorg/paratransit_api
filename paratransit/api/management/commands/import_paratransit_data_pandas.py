import sys,os
from django.core.management.base import BaseCommand, CommandError
from api.models import *
import csv
import pandas
import datetime
from django.db import connection
from django.conf import settings


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
		# location of file
		filename = os.path.join('/mnt/volume-nyc1-01/paratransit_raw_data/', 'paratransit_2015_vars.csv')

		df = pandas.read_csv(filename)

		user = settings.DATABASES['default']['USER']
		password = settings.DATABASES['default']['PASSWORD']
		database_name = settings.DATABASES['default']['NAME']

		database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
		    user=user,
		    password=password,
		    database_name=database_name,
		)

		engine = create_engine(database_url, echo=False)
		df.to_sql(trips, con=engine)

	def handle(self, *args, **options):
		print "Truncate Table...."
		self.truncate_table()
		print "Load Paratransit Data with Pandas..."
		self.load_paratransit_data()




