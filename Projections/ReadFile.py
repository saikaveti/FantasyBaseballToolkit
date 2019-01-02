from ProjectionPlayer import *

class ReadFile:
    def __init__(self, input_file):
        self.input_file = input_file

    def generate_players(self):

        lines = [line.rstrip('\n') for line in open(self.input_file)]


        list_players = list()

        first_name = ""
        last_name = ""

        Age = ""

        #Additional Variables
        R = 0
        RBI = 0
        SO = 0
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
            elif line.startswith("Age"):
                elements = line.split();
                Age = elements[1];
            elif line.startswith("AB"):
                elements = line.split()
                AB = int(elements[1])
                if AB < 10:
                    AB = 1000000
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
            elif line.startswith("R") and not line.startswith("RBI"):
                elements = line.split()
                R = int(elements[1])
            elif line.startswith("SO"):
                elements = line.split()
                SO = int(elements[1])
            elif line.startswith("RBI"):
                elements = line.split()
                RBI = int(elements[1])
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
                player = AdvancedPlayer(first_name, last_name, Age, AB, H, DOUBLE, TRIPLE, HR, BB, HBP, BA, OBP, SLG, OPS, IBB, SB, CS, GIDP, SH, SF, R, RBI, SO)
                if player.AB != 1000000:
                    list_players.append(player)


        return list_players
