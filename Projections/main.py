from WriteFiles import *
from ReadFile import *
from ProjectionHandler import *

import pandas as pd

writer = WriteData(2018, "stats_file.txt")
reader = ReadFile("stats_file.txt")

writer.write_data_to_text(3)
players3 = reader.generate_players()
writer.write_clean_data_to_csv(players3, "threeyears.csv")

writer.write_data_to_text(2)
players2 = reader.generate_players()
writer.write_clean_data_to_csv(players2, "twoyears.csv")

writer.write_data_to_text(1)
players1 = reader.generate_players()
writer.write_clean_data_to_csv(players1, "oneyear.csv")

writer.write_data_to_text(0)
players0 = reader.generate_players()
writer.write_clean_data_to_csv(players0, "currentyear.csv")

handler = ProjectionHandler("currentyear.csv", "oneyear.csv", "twoyears.csv", "threeyears.csv")
handler.create_map()
