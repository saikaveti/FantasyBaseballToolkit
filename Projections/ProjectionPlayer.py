from tabulate import tabulate


class AdvancedPlayer:

    def __init__(self, first_name, last_name, Age, AB, H, DOUBLE, TRIPLE, HR, BB, HBP, BA, OBP, SLG, OPS, IBB, SB, CS, GIDP, SH, SF, R, RBI, SO):
        self.first_name = first_name
        self.last_name = last_name
        self.Age = Age;
        #Extra Variables
        self.R = R
        self.RBI = RBI
        self.SO = SO
        #Taken Variables
        self.AB = AB
        self.H = H
        self.DOUBLE = DOUBLE
        self.TRIPLE = TRIPLE
        self.HR = HR
        self.BB = BB
        self.HBP = HBP
        self.IBB = IBB
        self.SB = SB
        self.CS = CS
        self.GIDP = GIDP
        self.SH = SH
        self.SF = SF
        #Needed Variables (Not Computed)
        self.BA = BA
        self.OBP = OBP
        self.SLG = SLG
        self.OPS = OPS
        #Intermediate Variables
        self.TB = H + DOUBLE + 2 * TRIPLE + 3 * HR
        self.RC = (float(H + BB + HBP - CS - GIDP) * float(self.TB + 0.26 * (BB - IBB + HBP) + 0.52 * (SH + SF + SB))) / (float(AB + BB + HBP + SH + SF))
        #Computed Variables
        self.TA = float(self.TB + BB + HBP + SB - CS) / float(AB - H + CS + GIDP)
        self.ISO = SLG - BA
        self.SECA = float(self.TB - H + BB + SB - CS) / float(AB)
        self.RC27 = self.RC / (float(AB - H + SH + SF + CS + GIDP) / 27.0)

    def print_player(self):
        print("First Name: {}, Last Name: {}, AB: {!s}, H: {!s}, 2B: {!s}, 3B: {!s}, HR: {!s}, BB: {!s}, HBP: {!s}, IBB: {!s}, SB: {!s}, CS: {!s}, GIDP: {!s}, SH: {!s}, SF: {!s}, BA: {!s}, OBP: {!s}, SLG: {!s}, OPS: {!s}, TB: {!s}, RC: {!s}, TA: {!s}, ISO: {!s}, SECA: {!s}, RC27: {!s}".format(self.first_name, self.last_name, self.AB, self.H, self.DOUBLE, self.TRIPLE, self.HR, self.BB, self.HBP, self.IBB, self.SB, self.CS, self.GIDP, self.SH, self.SF, self.BA, self.OBP, self.SLG, self.OPS, self.TB, self.RC, self.TA, self.ISO, self.SECA, self.RC27))
