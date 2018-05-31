from pybaseball import playerid_lookup
from pybaseball import batting_stats_range
from Player import *
from DateManipulation import *

import re

class StatsRange:

    def __init__(self, first_name, last_name, output_file):
        self.first_name = first_name
        self.last_name = last_name
        #self.playerid_array = playerid_lookup(last_name, first_name)
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

            #print(self.playerid)

    def create_player(self):
        lines = [line.rstrip('\n') for line in open(self.output_file)]

        full_name = self.first_name + " " + self.last_name

        player_found = False

        first_name = ""
        last_name = ""
        AB = 0
        R = 0
        H = 0
        HR = 0
        RBI = 0
        SO = 0
        SB = 0
        BA = 0.0
        OBP = 0.0
        OPS = 0.0
        SLG = 0.0

        #print(len(lines))

        for line in lines:
            if (line.startswith("Name") and not line.startswith("Name:")):
                #print(line)
                elements = re.split(r'\s{2,}', line)
                if full_name.lower() == elements[1].lower():
                    #print(full_name)
                    full_name = elements[1]

                    name_elements = full_name.split()
                    first_name = name_elements[0]
                    last_name = name_elements[1]

                    player_found = True

            if (player_found):
                if line.startswith("AB"):
                    elements = line.split()
                    AB = int(elements[1])
                elif line.startswith("R") and not line.startswith("RBI"):
                    elements = line.split()
                    R = int(elements[1])
                elif line.startswith("H") and not line.startswith("HR") and not line.startswith("HBP"):
                    elements = line.split()
                    H = int(elements[1])
                elif line.startswith("HR"):
                    elements = line.split()
                    HR = int(elements[1])
                elif line.startswith("RBI"):
                    elements = line.split()
                    RBI = int(elements[1])
                elif line.startswith("SO"):
                    elements = line.split()
                    SO = int(elements[1])
                elif line.startswith("SB"):
                    elements = line.split()
                    SB = int(elements[1])
                elif line.startswith("BA"):
                    elements = line.split()
                    BA = float(elements[1])
                elif line.startswith("OBP"):
                    elements = line.split()
                    OBP = float(elements[1])
                    #print("FIND LINE")
                elif line.startswith("SLG"):
                    elements = line.split()
                    SLG = float(elements[1])
                elif line.startswith("OPS"):
                    elements = line.split()
                    OPS = float(elements[1])
                elif line.startswith("Name:"):
                    player_found = False

        return Player(first_name, last_name, AB, R, H, HR, RBI, SO, SB, BA, OBP, SLG, OPS)

    def create_player_for_comp(self, first_name, last_name):
        lines = [line.rstrip('\n') for line in open(self.output_file)]

        full_name = first_name + " " + last_name

        player_found = False

        first_name = ""
        last_name = ""
        AB = 0
        R = 0
        H = 0
        HR = 0
        RBI = 0
        SO = 0
        SB = 0
        BA = 0.0
        OBP = 0.0
        OPS = 0.0
        SLG = 0.0

        #print(len(lines))

        for line in lines:
            if (line.startswith("Name") and not line.startswith("Name:")):
                #print(line)
                elements = re.split(r'\s{2,}', line)
                if full_name.lower() == elements[1].lower():
                    #print(full_name)
                    full_name = elements[1]

                    name_elements = full_name.split()
                    first_name = name_elements[0]
                    last_name = name_elements[1]

                    player_found = True

            if (player_found):
                if line.startswith("AB"):
                    elements = line.split()
                    AB = int(elements[1])
                elif line.startswith("R") and not line.startswith("RBI"):
                    elements = line.split()
                    R = int(elements[1])
                elif line.startswith("H") and not line.startswith("HR") and not line.startswith("HBP"):
                    elements = line.split()
                    H = int(elements[1])
                elif line.startswith("HR"):
                    elements = line.split()
                    HR = int(elements[1])
                elif line.startswith("RBI"):
                    elements = line.split()
                    RBI = int(elements[1])
                elif line.startswith("SO"):
                    elements = line.split()
                    SO = int(elements[1])
                elif line.startswith("SB"):
                    elements = line.split()
                    SB = int(elements[1])
                elif line.startswith("BA"):
                    elements = line.split()
                    BA = float(elements[1])
                elif line.startswith("OBP"):
                    elements = line.split()
                    OBP = float(elements[1])
                    #print("FIND LINE")
                elif line.startswith("SLG"):
                    elements = line.split()
                    SLG = float(elements[1])
                elif line.startswith("OPS"):
                    elements = line.split()
                    OPS = float(elements[1])
                elif line.startswith("Name:"):
                    player_found = False

        return Player(first_name, last_name, AB, R, H, HR, RBI, SO, SB, BA, OBP, SLG, OPS)

    def write_file_for_dates(self, prev_date, late_date):
        date_obj = DateManipulation()

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, late_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data

    def write_file_for_range(self, num_days):
        date_obj = DateManipulation()

        prev_date = date_obj.get_date_for_num_days(num_days)
        last_date = date_obj.get_date_for_num_days(1)

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

        player = self.create_player()

        player.print_player()

        return data

    def last_week(self):
        print("\nFINDING LAST WEEKS'S DATA:")

        data = self.write_file_for_range(7)

        player = self.create_player()

        player.print_player()

        return data

    def last_30_days(self):
        print("\nFINDING LAST MONTH'S DATA:")

        data = self.write_file_for_range(30)

        player = self.create_player()

        player.print_player()

    def ytd(self):
        print("\nFINDING YEAR TO DATE'S DATA:")

        date_obj = DateManipulation()

        prev_date = '2018-03-29'
        last_date = date_obj.get_date_for_num_days(2)

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        player = self.create_player()

        player.print_player()

        return data

    def driver(self):
        #self.parse_array()
        self.yesterday()
        self.last_week()
        self.last_30_days()
        self.ytd()
