from WriteFiles import *
from ReadFile import *

writer = WriteData(2017, "stats_file.txt")
reader = ReadFile("stats_file.txt")

writer.write_data_to_text(3)
players = reader.generate_players()
writer.write_clean_data_to_csv(players, "threeyears.csv")
