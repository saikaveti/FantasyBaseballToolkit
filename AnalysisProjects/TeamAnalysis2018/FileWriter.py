from pybaseball import batting_stats_range
from tabulate import tabulate

class WriteData:

    def __init__(self, year, output_file):
        self.year = year
        self.output_file = output_file

    def write_data_to_text(self, years_before):
        file = open(self.output_file, 'w')

        calc_year = self.year - years_before

        data = batting_stats_range(str(calc_year) + "-03-25", str(calc_year) + "-10-01")

        for i, row in data.iterrows():
            file.write(str(row))
            file.write("\n")

        file.close()

        return data

    def write_clean_data_to_csv(self, players, csv_file):
        file = open(csv_file, 'w')

        file.write("FIRST,LAST,Team,Age,AB,H,2B,3B,HR,RBI,SO,BB,HBP,IBB,SB,CS,GIDP,SH,SF,BA,OBP,SLG,OPS,TB,RC,TA,ISO,SECA,RC27")
        file.write("\n")

        for p in players:
            file.write(p.first_name + "," + p.last_name + "," + p.team + "," + p.Age + "," + str(p.AB) + "," + str(p.H) + "," + str(p.DOUBLE) + "," + str(p.TRIPLE) + "," + str(p.HR) + "," + str(p.RBI) + "," + str(p.SO) + "," + str(p.BB) + "," + str(p.HBP) + "," + str(p.IBB) + "," + str(p.SB) + "," + str(p.CS) + "," + str(p.GIDP) + "," + str(p.SH) + "," + str(p.SF) + "," + str(p.BA) + "," + str(p.OBP) + "," + str(p.SLG) + "," + str(p.OPS) + "," + str(p.TB) + "," + str(p.RC) + "," + str(p.TA) + "," + str(p.ISO) + "," + str(p.SECA) + "," + str(p.RC27))
            file.write("\n")

        file.close()
