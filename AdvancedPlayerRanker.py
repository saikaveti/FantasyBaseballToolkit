from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *
from PlayerComparison import *
from WriteData import *

from sklearn.decomposition import PCA

import numpy as np

import sys

class AdvancedPlayerRanker:

    def __init__(self, num_days, output_file):
        self.num_days = num_days
        self.output_file = output_file

    def write_file_for_range(self):
        date_obj = DateManipulation()

        prev_date = date_obj.get_date_for_num_days(self.num_days)
        last_date = date_obj.get_previous_date()

        #print(prev_date)

        file = open(self.output_file, 'w')

        data = batting_stats_range(prev_date, last_date)

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data

    def generate_players(self):
        self.write_file_for_range()

        lines = [line.rstrip('\n') for line in open(self.output_file)]


        list_players = list()
        pruned_list_players = list()

        first_name = ""
        last_name = ""

        #Taken Variables
        AB = 0
        H = 0
        DOUBLE = 0
        TRIPLE = 0
        HR = 0
        BB = 0
        HBP = 0
        BB = 0
        IBB = 0
        HBP = 0
        SB = 0
        CS = 0
        GIDP = 0
        SH = 0
        SF = 0
        #Needed Variables (Not Computed)
        BA = 0.0
        OBP = 0.0
        SLG = 0.0
        OPS = 0.0



        for line in lines:
			###print(line)
            if line.startswith("Name") and not line.startswith("Name:"):
                elements = line.split()
                first_name = elements[1]
                last_name = elements[2]
            elif line.startswith("AB"):
                elements = line.split()
                AB = int(elements[1])
                if int(elements[1]) >= 0 and int(elements[1]) <= 10:
                    AB = -1000000
            elif line.startswith("H") and not line.startswith("HR") and not line.startswith("HBP"):
                elements = line.split()
                H = int(elements[1])
            elif line.startswith("2B"):
                elements = line.split()
                DOUBLE = int(elements[1])
            elif line.startswith("3B"):
                elements = line.split()
                TRIPLE = int(elements[1])
            elif line.startswith("HR"):
                elements = line.split()
                HR = int(elements[1])
            elif line.startswith("BB"):
                elements = line.split()
                BB = int(elements[1])
            elif line.startswith("HBP"):
                elements = line.split()
                HBP = int(elements[1])
            elif line.startswith("BB"):
                elements = line.split()
                BB = int(elements[1])
            elif line.startswith("IBB"):
                elements = line.split()
                IBB = int(elements[1])
            elif line.startswith("HBP"):
                elements = line.split()
                HBP = int(elements[1])
            elif line.startswith("SB"):
                elements = line.split()
                SB = int(elements[1])
            elif line.startswith("CS"):
                elements = line.split()
                CS = int(elements[1])
            elif line.startswith("GIDP"):
                elements = line.split()
                GIDP = int(elements[1])
            elif line.startswith("SH"):
                elements = line.split()
                SH = int(elements[1])
            elif line.startswith("SF"):
                elements = line.split()
                SF = int(elements[1])
            elif line.startswith("BA"):
                elements = line.split()
                BA = float(elements[1])
            elif line.startswith("OBP"):
                elements = line.split()
                OBP = float(elements[1])
            elif line.startswith("SLG"):
                elements = line.split()
                SLG = float(elements[1])
            elif line.startswith("OPS"):
                elements = line.split()
                OPS = float(elements[1])
            elif line.startswith("Name:"):
                player = AdvancedPlayer(first_name, last_name, AB, H, DOUBLE, TRIPLE, HR, BB, HBP, BA, OBP, SLG, OPS, IBB, SB, CS, GIDP, SH, SF)
                list_players.append(player)

        for player in list_players:
            if (player.AB != -1000000):
                pruned_list_players.append(player)

        return pruned_list_players

    def get_opg_player_list(self, list_players):
        write_data = WriteData(list_players, "raw_data.csv")
        write_data.write_player_data()

        BA_values = np.array([])
        OBP_values = np.array([])
        SLG_values = np.array([])
        OPS_values = np.array([])
        TA_values = np.array([])
        ISO_values = np.array([])
        SECA_values = np.array([])
        RC27_values = np.array([])

        for player in list_players:
            BA_values = np.append(BA_values, player.BA)
            OBP_values = np.append(OBP_values, player.OBP)
            SLG_values = np.append(SLG_values, player.SLG)
            OPS_values = np.append(OPS_values, player.OPS)
            TA_values = np.append(TA_values, player.TA)
            ISO_values = np.append(ISO_values, player.ISO)
            SECA_values = np.append(SECA_values, player.SECA)
            RC27_values = np.append(RC27_values, player.RC27)

        BA_mean = np.mean(BA_values)
        OBP_mean = np.mean(OBP_values)
        SLG_mean = np.mean(SLG_values)
        OPS_mean = np.mean(OPS_values)
        TA_mean = np.mean(TA_values)
        ISO_mean = np.mean(ISO_values)
        SECA_mean = np.mean(SECA_values)
        RC27_mean = np.mean(RC27_values)

        BA_std = np.std(BA_values)
        OBP_std = np.std(OBP_values)
        SLG_std = np.std(SLG_values)
        OPS_std = np.std(OPS_values)
        TA_std = np.std(TA_values)
        ISO_std = np.std(ISO_values)
        SECA_std = np.std(SECA_values)
        RC27_std = np.std(RC27_values)

    def get_ranked_players(self, start_rank, end_rank):
        list_players = self.generate_players()
        self.get_opg_player_list(list_players)
