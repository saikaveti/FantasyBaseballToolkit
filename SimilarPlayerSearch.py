from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *
from PlayerComparison import *

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

    def isSimilarTo(self, main_player, player, min_similarities):
        count = 0

        minRun = main_player.R * .85
        maxRun = main_player.R * 1.15

        if (player.R > minRun and player.R < maxRun):
            count += 1

        minHits = main_player.H * .8
        maxHits = main_player.H * 1.2

        if (player.H > minHits and player.H < maxHits):
            count += 1

        minHR = main_player.HR * .7
        maxHR = main_player.HR * 1.3

        if (player.HR > minHR and player.HR < maxHR):
            count += 1

        minRBI = main_player.RBI * .75
        maxRBI = main_player.RBI * 1.25

        if (player.RBI > minRBI and player.RBI < maxRBI):
            count += 1

        minSO = main_player.SO * .6
        maxSO = main_player.SO * 1.4

        if (player.SO > minSO and player.SO < maxSO):
            count += 1

        minSB = main_player.SB * .9
        maxSB = main_player.SB * 1.1

        if (player.SB > minSB and player.SB < maxSB):
            count += 1

        minBA = main_player.BA - .050
        maxBA = main_player.BA + .050

        if (player.BA > minBA and player.BA < maxBA):
            count += 1

        minOBP = main_player.OBP - .050
        maxOBP = main_player.OBP + .050

        if (player.OBP > minOBP and player.OBP < maxOBP):
            count += 1

        minSLG = main_player.SLG - .075
        maxSLG = main_player.SLG + .075

        if (player.SLG > minSLG and player.SLG < maxSLG):
            count += 1

        minOPS = main_player.OPS - .125
        maxOPS = main_player.OPS + .125

        if (player.OPS > minOPS and player.OPS < maxOPS):
            count += 1

        if (count < min_similarities):
            return False
        else:
            return True

    def find_similar_players(self, min_similarities):
        self.write_file_for_range()

        list = self.create_player_list()

        main_player = Player("", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        for player in list:
            if (player.first_name.lower() == self.first_name and player.last_name.lower() == self.last_name):
                main_player = player
                break

        similar_player_list = []

        similar_player_list.append(main_player)

        for player in list:
            if (self.isSimilarTo(main_player, player, min_similarities)):
                if (main_player.first_name.lower() != player.first_name.lower() and main_player.last_name.lower() != player.last_name.lower()):
                    similar_player_list.append(player)

        first_name_list = []
        last_name_list = []

        for player in similar_player_list:
            first_name_list.append(player.first_name)
            last_name_list.append(player.last_name)

        comparison = PlayerComparison(first_name_list, last_name_list, self.num_days, self.output_file, "", "")
        comparison.list_players = similar_player_list

        comparison.tabulate_players(False)
