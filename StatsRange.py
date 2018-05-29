from pybaseball import playerid_lookup
from pybaseball import batting_stats_range
from DateManipulation import *

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

            #print(len(lines))

            for line in lines:
                if (line.startswith("key_mlbam")):
                    array = line.split()
                    self.playerid = int(array[1])

            print(self.playerid)

    def create_player(self):
        lines = [line.rstrip('\n') for line in open(self.input_data_file)]

        list = []

        first_name = ""
        last_name = ""
        PA = 0
        AB = 0
        R = 0
        H = 0
        HR = 0
        RBI = 0
        SO = 0
        SB = 0
        BA = 0
        OPB = 0
        OPS = 0
        SLG = 0 

    def write_file_for_range(self, num_days):
        date_obj = DateManipulation()

        prev_date = date_obj.get_date_for_num_days(num_days)
        last_date = date_obj.get_previous_date()

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data

    def yesterday(self):
        print("FINDING YESTERDAY'S DATA:")

        data = self.write_file_for_range(1)

        return data


    def last_week(self):
        print("FINDING LAST WEEKS'S DATA:")

        data = self.write_file_for_range(7)

        return data

    def last_30_days(self):
        print("FINDING LAST MONTH'S DATA:")

        data = self.write_file_for_range(1)

        return data

    def ytd(self):
        print("FINDING YEAR TO DATE'S DATA:")

        date_obj = DateManipulation()

        prev_date = '2018-03-29'
        last_date = date_obj.get_previous_date()

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data


    def driver(self):
        self.parse_array()
        self.yesterday()
        self.last_week()
        self.last_30_days()
        self.ytd()
