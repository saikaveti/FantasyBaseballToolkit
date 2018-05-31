from StatsRange import *

stats_file = "stats_file.txt"

### TO REDUCE TYPING WHILE TESTING

###first_name = raw_input("First Name: ")
###last_name = raw_input("Last Name: ")

first_name = "j.d."
last_name = "martinez"

main_stats = StatsRange(first_name, last_name, stats_file)
main_stats.driver()
