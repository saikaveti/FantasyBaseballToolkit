from pybaseball import batting_stats_range
from tabulate import tabulate

class WriteData:

    def __init__(self, year, output_file):
        self.year = year
        self.output_file = output_file

    def write_data_to_text(self, years_before):
        file = open(self.output_file, 'w')

        calc_year = self.year - years_before

        print(str(calc_year) + "-03-25")

        data = batting_stats_range(str(calc_year) + "-03-25", str(calc_year) + "-10-01")

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data
