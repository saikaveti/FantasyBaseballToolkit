from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *

class SimilarPlayerSearch:

    def __init__(self, first_name, last_name, num_days, output_file):
        self.first_name = first_name
        self.last_name = last_name
        self.num_days = num_days
        self.output_file = output_file

    def write_file_for_range(self):
        date_obj = DateManipulation()

        prev_date = date_obj.get_date_for_num_days(self.num_days)
        last_date = date_obj.get_date_for_num_days(1)

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

            file.close()

            return data

    def create_player_list(self):
        lines = [line.rstrip('\n') for line in open(self.output_file)]

        list_players = list()

        first_name_find = ""
        last_name_find = ""
        AB = 0
        R = 0
        H = 0
        HR = 0
        SO = 0
        SB = 0
        BA = 0.0
        OBP = 0.0
        SLG = 0.0
        OPS = 0.0

        for line in lines:

			###print(line)
            if line.startswith("Name") and not line.startswith("Name:"):
                elements = line.split()
                first_name_find = elements[1]
                last_name_find = elements[2]
            elif line.startswith("AB"):
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
                player = Player(first_name_find, last_name_find, AB, R, H, HR, RBI, SO, SB, BA, OBP, SLG, OPS)
                list_players.append(player)

        return list_players

    def find_similar_players(self):
        list = self.create_player_list()

        main_player = Player("", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        for player in list:
            if (player.first_name.lower() == self.first_name && player.last_name.lower() == self.last_name):
                main_player = player
                break

        similar_player_list = list()

        for player in list:
