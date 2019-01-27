from FileReader import *
from FileWriter import *
from Player import *

writer = WriteData(2018, "stats_file.txt")
reader = ReadFile("stats_file.txt")

writer.write_data_to_text(0)
players0 = reader.generate_players()
writer.write_clean_data_to_csv(players0, "data.csv")
