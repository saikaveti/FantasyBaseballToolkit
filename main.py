from StatsRange import *
from PlayerComparison import *
from SimilarPlayerSearch import *

stats_file = "stats_file.txt"

### TO REDUCE TYPING WHILE TESTING

###first_name = raw_input("First Name: ")
###last_name = raw_input("Last Name: ")

first_name = "jed"
last_name = "lowrie"

main_stats = StatsRange(first_name, last_name, stats_file)
###ain_stats.driver()

compare_stats = PlayerComparison(["j.d.", "rafael"], ["martinez", "devers"], 14, stats_file, "", "")
###compare_stats.tabulate_players()

similarPlayers = SimilarPlayerSearch("jed", "lowrie", 14, stats_file)
similarPlayers.find_similar_players()
