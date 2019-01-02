import pandas as pd
import numpy as np

class ProjectionHandler:
    def __init__(self, currentyear, currentList, oneyear, oneList, twoyears, twoList, threeyears, threeList):
        self.currentyearDF = pd.read_csv(currentyear)
        self.oneyearDF = pd.read_csv(oneyear)
        self.twoyearDF = pd.read_csv(twoyears)
        self.threeyearDF = pd.read_csv(threeyears)

        self.currentyearList = currentList
        self.oneyearList = oneList
        self.twoyearList = twoList
        self.threeyearList = threeList

        self.oneyearDict = {}
        self.twoyearsDict = {}
        self.threeyearsDict = {}

    def get_map(self, list):
        my_dict = {}
        for p in list:
            my_dict[p.first_name + " " + p.last_name] = p

        return my_dict

    def create_dicts(self):
        self.oneyearDict = self.get_map(self.oneyearList);
        self.twoyearsDict = self.get_map(self.twoyearList);
        self.threeyearsDict = self.get_map(self.threeyearList);
