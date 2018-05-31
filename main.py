from StatsRange import *
from PlayerComparison import *

stats_file = "stats_file.txt"

### TO REDUCE TYPING WHILE TESTING

###first_name = raw_input("First Name: ")
###last_name = raw_input("Last Name: ")

first_name = "paul"
last_name = "goldschmidt"

main_stats = StatsRange(first_name, last_name, stats_file)
main_stats.driver()

compare_stats = PlayerComparison(["j.d.", "rafael"], ["martinez", "devers"], 0, stats_file, "2018-04-16", "2018-04-18")
compare_stats.tabulate_players()
