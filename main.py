from StatsRange import *
from PlayerComparison import *
from SimilarPlayerSearch import *
from AdvancedPlayerRanker import *

import sys


stats_file = "stats_file.txt"

type_analysis = "ranked"

first_name = "paul"
last_name = "goldschmidt"

### TO REDUCE TYPING WHILE TESTING

###first_name = raw_input("First Name: ")
###last_name = raw_input("Last Name: ")

if type_analysis == "range":
    main_stats = StatsRange(first_name, last_name, stats_file)
    main_stats.driver()

if type_analysis == "comparison":
    compare_stats = PlayerComparison(["j.d.", first_name], ["martinez", last_name], 14, stats_file, "", "")
    compare_stats.tabulate_players(True)

if type_analysis == "similar":
    similarPlayers = SimilarPlayerSearch(first_name, last_name, 14, stats_file)
    similarPlayers.find_similar_players(7)

if type_analysis == "ranked":
    rankedPlayers = AdvancedPlayerRanker(200, stats_file)
    rankedPlayers.get_ranked_players(1, 25);
