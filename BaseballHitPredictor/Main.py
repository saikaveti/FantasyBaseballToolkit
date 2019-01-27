import datetime
from RetrieveData import *
from PlayerList import *
from WriteData import *
from LogisticRegression import *


write_data_object = RetrieveData(datetime.datetime.now())

###print(read.list_of_dates())
print()

date = write_data_object.get_current_date_only()

write_data_object.write_batting_for_date("playerdatatable.txt")
write_data_object.write_batting_for_single_date("PlayerHitStat.txt")

playerlist = PlayerList("playerdatatable.txt", "PlayerHitStat.txt")

list = playerlist.prune_list()


final_data = WriteData(list, "BaseballLearningTable.csv")
final_data.write_player_data()

regression = Classifier("BaseballLearningTable.csv")
regression.perform_regression()
