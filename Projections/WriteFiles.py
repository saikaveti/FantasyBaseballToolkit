from pybaseball import batting_stats_range
from tabulate import tabulate

class WriteData:

    def __init__(self, year):
		self.year = year

    def write_data_to_text(self, year):
        file = open("stats_file.txt", 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data
