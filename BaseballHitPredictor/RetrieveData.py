from pybaseball import batting_stats_range
from datetime import date, timedelta
import datetime
import re

class RetrieveData:

	def __init__(self, date):
		self.current_date = date

	def get_date(self):
		return self.current_date

	def list_of_dates(self):
		current_str = str(self.current_date)
		args = current_str.split()

		date_only = args[0]

		date_elements = re.split('[-]', date_only)

		first_date = date(2018, 3, 29)
		last_date = date(int(date_elements[0]), int(date_elements[1]), int(date_elements[2]))

		delta = last_date - first_date

		valid_dates = []

		for i in range(delta.days):
    			valid_dates.append(str(first_date + timedelta(days = i)))

		return valid_dates

	def get_current_date_only(self):
		current_str = str(self.current_date)
		args = current_str.split()
		date_only = args[0]
		return date_only

	def write_batting_for_date(self, outputfile):
		print(self.find_prev_date())
		data = batting_stats_range("2018-03-29", self.find_prev_date())

		file = open(outputfile, 'w')

		for i, row in data.iterrows():
			file.write(str(row))
			file.write("\n")

		file.close()

		return data

	def find_prev_date(self):
		prev_date = datetime.datetime.now() - timedelta(days = 1)

		prev_str = str(prev_date)
		args = prev_str.split()
		date_only = args[0]

		return date_only

	def write_batting_for_single_date(self, output_file):
		data = batting_stats_range(self.find_prev_date(),)

		file = open(output_file, 'w')

		for i, row in data.iterrows():
			file.write(str(row))
			file.write("\n")

		file.close()

		return data
