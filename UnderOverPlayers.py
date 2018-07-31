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

        X = pd.DataFrame(obj)

        X = X.drop(columns = ['OBP', 'SLG', 'TA', 'SECA', 'FIRST_NAME', "LAST_NAME", "RC27"]).astype(float)

        num = 5

        clf = KMeans(n_clusters = num)
        clf.fit(X)

        cluster_map = pd.DataFrame()
        cluster_map['data_index'] = X.index.values
        cluster_map['cluster'] = clf.labels_

        complete_underrated = list()


        for i in range(num):
            mapping = cluster_map[cluster_map.cluster == i]
            list_indexes = list()

            for index, row in mapping.iterrows():
                list_indexes.append(row['data_index'])

            total_values = X.values.tolist()

            list_cluster = list()

            for index in list_indexes:
                temp_value = total_values[index]

                for player in list_players:
                    if temp_value[0] == player.BA and temp_value[1] == player.OPS and temp_value[2] == player.ISO:
                        list_cluster.append(player)


            size = len(list_cluster)

            total_RC27 = 0.0

            for player in list_cluster:
                total_RC27 += player.RC27

            average_RC27 = total_RC27 / size

            for player in list_cluster:
                if player.RC27 < average_RC27:

                    if (average_RC27 - player.RC27) / average_RC27 > .1:
                        complete_underrated.append(player)

        return complete_underrated

    def tabulate_under_players(self):
        total_players = self.get_players()

        babip_players = self.prune_on_BABIP(total_players)
        clustering_players = self.prune_on_clustering(total_players)

        final_list = babip_players

        for player in clustering_players:
            final_list.append(player)


        first_name_list = list()
        last_name_list = list()


        for player in final_list:
            first_name_list.append(player.first_name)
            last_name_list.append(player.last_name)

        comparison = PlayerComparison(first_name_list, last_name_list, self.num_days, self.output_file, "", "")
        comparison.list_players = final_list
        comparison.tabulate_players(False)
