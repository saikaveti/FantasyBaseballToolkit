from pybaseball import statcast_batter
from pybaseball import playerid_lookup

class StatsRange:

    def __init__(self, first_name, last_name, output_file):
        self.first_name = first_name
        self.last_name = last_name
        self.playerid_array = playerid_lookup(last_name, first_name)
        self.playerid = 0
        self.output_file = output_file

    def parse_array(self):

        file = open("parse_array_file.txt", 'w')

        if (len(self.playerid_array) != 1):
            print("Invalid Entry")
        else:
            for row in self.playerid_array.iterrows():
                file.write(str(row))
                file.write("\n")

            file.close()

            with open('parse_array_file.txt') as f:
                lines = f.readlines()

            ### print(len(lines))

            for line in lines:
                if (line.startswith("key_mlbam")):
                    array = line.split()
                    self.playerid = int(array[1])

            ### print(self.playerid)

    def yesterday(self):
        print("FINDING YESTERDAY'S DATA:")

    def yesterday(self):
        print("FINDING LAST WEEKS'S DATA:")

    def yesterday(self):
        print("FINDING LAST MONTH'S DATA:")

    def yesterday(self):
        print("FINDING YEAR TO DATE'S DATA:")


    def driver(self):
        self.parse_array()
        self.yesterday()
        self.last_week()
        self.last_month()
        self.ytd()
