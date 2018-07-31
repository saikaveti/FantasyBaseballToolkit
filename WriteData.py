class WriteData:
	def __init__(self, list, output_file):
		self.player_list = list
		self.output_file = output_file

	def write_player_data(self):
		file = open(self.output_file, 'w')

		header = ("BA,OBP,SLG,OPS,TA,ISO,SECA,RC27")
		file.write(header)
		file.write("\n")

		for p in self.player_list:
			line = str(p.BA) + "," + str(p.OBP) + "," + str(p.SLG) + "," + str(p.OPS) + "," + str(p.TA) + "," + str(p.ISO) + "," + str(p.SECA) + "," + str(p.RC27)
			file.write(line)
			file.write("\n")

		file.close()

	def write_extended_player_data(self):
		file = open(self.output_file, 'w')

		header = ("FIRST_NAME,LAST_NAME,BA,OBP,SLG,OPS,TA,ISO,SECA,RC27")
		file.write(header)
		file.write("\n")

		for p in self.player_list:
			line = p.first_name + "," + p.last_name + "," + str(p.BA) + "," + str(p.OBP) + "," + str(p.SLG) + "," + str(p.OPS) + "," + str(p.TA) + "," + str(p.ISO) + "," + str(p.SECA) + "," + str(p.RC27)
			file.write(line)
			file.write("\n")
