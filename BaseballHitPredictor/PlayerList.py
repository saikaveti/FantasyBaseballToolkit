from Player import *
from PlayerSingleDay import *
from RetrieveData import *
import datetime
import re

class PlayerList:
	def __init__(self, readfile, singlefile):
		self.readfile = readfile
		self.singlefile = singlefile

	def create_list(self):
		lines = [line.rstrip('\n') for line in open(self.readfile)]


		list_players = list()
		pruned_list_players = list()

		first_name = ""
		last_name = ""

        #Taken Variables
		AB = 0
		H = 0
		DOUBLE = 0
		TRIPLE = 0
		HR = 0
		BB = 0
		HBP = 0
		BB = 0
		IBB = 0
		HBP = 0
		SB = 0
		CS = 0
		GIDP = 0
		SH = 0
		SF = 0
        #Needed Variables (Not Computed)
		BA = 0.0
		OBP = 0.0
		SLG = 0.0
		OPS = 0.0

		for line in lines:
			###print(line)
			if line.startswith("Name") and not line.startswith("Name:"):
				elements = line.split()
				first_name = elements[1]
				last_name = elements[2]
			elif line.startswith("AB"):
				elements = line.split()
				AB = int(elements[1])
				if int(elements[1]) >= 0 and int(elements[1]) <= 10:
					AB = -1000000
			elif line.startswith("H") and not line.startswith("HR") and not line.startswith("HBP"):
				elements = line.split()
				H = int(elements[1])
			elif line.startswith("2B"):
				elements = line.split()
				DOUBLE = int(elements[1])
			elif line.startswith("3B"):
				elements = line.split()
				TRIPLE = int(elements[1])
			elif line.startswith("HR"):
				elements = line.split()
				HR = int(elements[1])
			elif line.startswith("BB"):
				elements = line.split()
				BB = int(elements[1])
			elif line.startswith("HBP"):
				elements = line.split()
				HBP = int(elements[1])
			elif line.startswith("BB"):
				elements = line.split()
				BB = int(elements[1])
			elif line.startswith("IBB"):
				elements = line.split()
				IBB = int(elements[1])
			elif line.startswith("HBP"):
				elements = line.split()
				HBP = int(elements[1])
			elif line.startswith("SB"):
				elements = line.split()
				SB = int(elements[1])
			elif line.startswith("CS"):
				elements = line.split()
				CS = int(elements[1])
			elif line.startswith("GIDP"):
				elements = line.split()
				GIDP = int(elements[1])
			elif line.startswith("SH"):
				elements = line.split()
				SH = int(elements[1])
			elif line.startswith("SF"):
				elements = line.split()
				SF = int(elements[1])
			elif line.startswith("BA"):
				elements = line.split()
				BA = float(elements[1])
			elif line.startswith("OBP"):
				elements = line.split()
				OBP = float(elements[1])
			elif line.startswith("SLG"):
				elements = line.split()
				SLG = float(elements[1])
			elif line.startswith("OPS"):
				elements = line.split()
				OPS = float(elements[1])
			elif line.startswith("Name:"):
				player = Player(first_name, last_name, AB, H, DOUBLE, TRIPLE, HR, BB, HBP, BA, OBP, SLG, OPS, IBB, SB, CS, GIDP, SH, SF, 0)
				list_players.append(player)

		for player in list_players:
			if (player.AB != -1000000):
				pruned_list_players.append(player)

		return pruned_list_players

	def add_hit_stat(self):
		lines = [line.rstrip('\n') for line in open(self.singlefile)]
		list = []

		first_name = ""
		last_name = ""
		hit = 0

		for line in lines:
			if line.startswith("Name") and not line.startswith("Name:"):
				elements = line.split()
				###print(elements)
				###print("Name Found!")
				first_name = elements[1]
				last_name = elements[2]
			elif line.startswith("H") and not line.startswith("HR") and not line.startswith("HBP"):
				elements = line.split()
				###print(int(elements[1]))
				###print("Hits Found!")
				hits = int(elements[1])
				if (hits == 0):
					hit = 0
				else:
					hit = 1
			elif line.startswith("Name:"):
				player = PlayerSingleDay(first_name, last_name, hit)
				###print("CREATING PLAYER")
				list.append(player)
		return list

	def merge_lists(self):
		player_list = self.create_list()
		hit_list = self.add_hit_stat()

		for player in player_list:
			###print("IN LOOP")
			for single_day in hit_list:
				if player.first_name == single_day.first_name and player.last_name == single_day.last_name:
					player.get_hit = single_day.hit
		return player_list

	def prune_list(self):

		list  = self.merge_lists()

		retrieve = RetrieveData(datetime.datetime.now())

		list_dates = retrieve.list_of_dates()

		number_of_dates = len(list_dates)

		list = [x for x in list if not x.H < number_of_dates * .25]

		return list
