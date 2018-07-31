from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *
from PlayerComparison import *
from WriteData import *
from AdvancedPlayerRanker import *

import numpy as np
import pandas as pd
from matplotlib import style
from sklearn.cluster import KMeans

class UnderValuedPlayers:
    def __init__(self, num_days, output_file):
        self.num_days = num_days
        self.output_file = output_file

    def get_players(self):
        ranked = AdvancedPlayerRanker(self.num_days, self.output_file)

        return ranked.generate_players()

    def prune_on_BABIP(self, list_players):
        babip_pruned = list()

        for player in list_players:
            numerator = float(player.H - player.HR)
            denominator = float(player.AB - player.SO - player.HR + player.SF)

            babip = numerator/denominator

            if (babip < .250 and player.BA > .230):
                babip_pruned.append(player)

        return babip_pruned

    def prune_on_clustering(self, list_players):
        write_data = WriteData(list_players, "raw_data.csv")
        write_data.write_extended_player_data()

        obj = pd.read_csv("raw_data.csv")

        print(obj)


        X = obj.ix[2, 5]

        kmeans=KMeans(n_clusters=5, init='k-means++', max_iter= 300, n_init= 10, random_state= 0)
        kmeans.fit(X)

        #df.drop(['OBP', 'SLG', 'TA', 'SECA'])



    def tabulate_under_players(self):
        total_players = self.get_players()
        babip_players = self.prune_on_BABIP(total_players)

        self.prune_on_clustering(total_players)

        final_list = babip_players

        first_name_list = list()
        last_name_list = list()


        for player in final_list:
            first_name_list.append(player.first_name)
            last_name_list.append(player.last_name)

        comparison = PlayerComparison(first_name_list, last_name_list, self.num_days, self.output_file, "", "")
        comparison.list_players = final_list
        comparison.tabulate_players(False)
