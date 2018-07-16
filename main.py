from StatsRange import *
from PlayerComparison import *
from SimilarPlayerSearch import *
import sys


stats_file = "stats_file.txt"

### TO REDUCE TYPING WHILE TESTING

###first_name = raw_input("First Name: ")
###last_name = raw_input("Last Name: ")

first_name = "mike"
last_name = "trout"

main_stats = StatsRange(first_name, last_name, stats_file)
#main_stats.driver()

compare_stats = PlayerComparison(["j.d.", "mike"], ["martinez", "trout"], 14, stats_file, "", "")
#compare_stats.tabulate_players(True)

similarPlayers = SimilarPlayerSearch("mike", "trout", 14, stats_file)
similarPlayers.find_similar_players(7)
