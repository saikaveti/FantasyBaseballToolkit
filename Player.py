class Player:
    def __init__(self, first_name, last_name, AB, R, H, HR, RBI, SO, SB, BA, OBP, SLG, OPS):
        self.first_name = first_name
        self.last_name = last_name
        self.AB = AB
        self.R = R
        self.H = H
        self.HR = HR
        self.RBI = RBI
        self.SO = SO
        self.SB = SB
        self.BA = BA
        self.OBP = OBP
        self.OPS = OPS
        self.SLG = SLG

    def print_player(self):
        print(self.first_name + " " + self.last_name + ": " + str(self.AB)  + ", " + str(self.R)  + ", " + str(self.H)  + ", " + str(self.HR) + ", " + str(self.RBI) + ", " + str(self.SO) + ", " + str(self.SB) + ", " + str(self.BA) + ", " + str(self.OBP) + ", " + str(self.SLG) + ", " + str(self.OPS))
