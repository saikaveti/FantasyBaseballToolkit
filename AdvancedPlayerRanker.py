from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *
from PlayerComparison import *
from WriteData import *

from sklearn.decomposition import PCA
from sklearn import preprocessing

import numpy as np
import pandas as pd

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

        #Additional Variables
        R = 0
        RBI = 0
        SO = 0
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
                if int(elements[1]) >= 0 and int(elements[1]) <= self.num_days:
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
            elif line.startswith("R") and not line.startswith("RBI"):
                elements = line.split()
                R = int(elements[1])
            elif line.startswith("SO"):
                elements = line.split()
                SO = int(elements[1])
            elif line.startswith("RBI"):
                elements = line.split()
                RBI = int(elements[1])
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
                player = AdvancedPlayer(first_name, last_name, AB, H, DOUBLE, TRIPLE, HR, BB, HBP, BA, OBP, SLG, OPS, IBB, SB, CS, GIDP, SH, SF, R, RBI, SO)
                list_players.append(player)

        for player in list_players:
            if (player.AB != -1000000):
                pruned_list_players.append(player)

        return pruned_list_players

    def get_opg_player_list(self, list_players):

        write_data = WriteData(list_players, "raw_data.csv")
        write_data.write_player_data()

        df = pd.read_csv("raw_data.csv")

        x = df.values #returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        data = pd.DataFrame(x_scaled)

        pca = PCA(.95)
        pca.fit(data)

        df = pca.transform(df)

        pc = pca.components_

        pc1 = pc[0]

        print(pc1)

        opg_players  = list()

        for player in list_players:
            OPG =  (pc1[0]*player.BA + pc1[1]*player.OBP + pc1[2]*player.SLG + pc1[3]*player.OPS + pc1[4]*player.TA + pc1[5]*player.ISO + pc1[6]*player.SECA + pc1[7]*player.RC27)
            opg_player = OPGPlayer(player.first_name, player.last_name, OPG)
            opg_players.append(opg_player)

        return opg_players

    def get_ranked_players(self, start_rank, end_rank):
        list_players = self.generate_players()

        opg_players = self.get_opg_player_list(list_players)

        sort_list = sorted(opg_players, key = lambda x: x.OPG_score, reverse=True)

        partial_list = sort_list[start_rank - 1:end_rank]

        first_name_list = list()
        last_name_list = list()

        tabulate_players = list()

        for player in partial_list:
            first_name_list.append(player.first_name)
            last_name_list.append(player.last_name)

        for player in partial_list:
            for main_player in list_players:
                if player.first_name == main_player.first_name and player.last_name == main_player.last_name:
                    tabulate_players.append(main_player)

        comparison = PlayerComparison(first_name_list, last_name_list, self.num_days, self.output_file, "", "")
        comparison.list_players = tabulate_players
        comparison.tabulate_players(False)
