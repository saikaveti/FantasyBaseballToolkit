from WriteFiles import *
from ReadFile import *

writer = WriteData(2017, "stats_file.txt")
reader = ReadFile("stats_file.txt")

writer.write_data_to_text(3)
players = reader.generate_players()
writer.write_clean_data_to_csv(players, "threeyears.csv")

writer.write_data_to_text(2)
players = reader.generate_players()
writer.write_clean_data_to_csv(players, "twoyears.csv")

writer.write_data_to_text(1)
players = reader.generate_players()
writer.write_clean_data_to_csv(players, "oneyear.csv")

writer.write_data_to_text(0)
players = reader.generate_players()
writer.write_clean_data_to_csv(players, "currentyear.csv")
