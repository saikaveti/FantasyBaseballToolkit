from pybaseball import batting_stats_range
from tabulate import tabulate
from Player import *
from StatsRange import *
from DateManipulation import *

import sys

class PlayerComparison:
    def __init__(self, first_name_list, last_name_list, period_days, output_file, first_date, second_date):
        self.list_first_name = first_name_list
        self.list_last_name = last_name_list
        self.period_days = period_days
        self.output_file = output_file
        self.first_date = first_date
        self.second_date = second_date
        self.list_players = []

    def create_list_of_players(self):

        list_players = []

        for i, first_name in enumerate(self.list_first_name):
            range = StatsRange(first_name, self.list_last_name[i], self.output_file)

            if (self.period_days == 0):
                range.write_file_for_dates(self.first_date, self.second_date)
            else:
                range.write_file_for_range(self.period_days)

            player = range.create_player_for_comp(first_name, self.list_last_name[i])

            list_players.append(player)

        self.list_players = list_players



    def tabulate_players(self, generate_players):

        list = []

        if generate_players:
            self.create_list_of_players()

        list = self.list_players

        print("")

        if (self.period_days == 0):
            print("STATISTICS FROM " + self.first_date + " TO " + self.second_date)
        else:
            print("STATISTICS FOR LAST " + str(self.period_days) + " DAYS")

        titles = ["First Name", "Last Name" , "AB", "R", "H", "HR", "RBI", "SO", "SB", "BA", "OBP", "SLG", "OPS"]

        width = len(titles)
        height = len(list)

        array = [[0 for x in range(width)] for y in range(height)]

        for i, player in enumerate(list):
            array[i][0] = player.first_name
            array[i][1] = player.last_name
            array[i][2] = player.AB
            array[i][3] = player.R
            array[i][4] = player.H
            array[i][5] = player.HR
            array[i][6] = player.RBI
            array[i][7] = player.SO
            array[i][8] = player.SB
            array[i][9] = player.BA
            array[i][10] = player.OBP
            array[i][11] = player.SLG
            array[i][12] = player.OPS

        print(tabulate(array, headers = titles))
        print("")
