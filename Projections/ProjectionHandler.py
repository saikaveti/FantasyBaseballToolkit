import pandas as pd
import numpy as np

class ProjectionHandler:
    def __init__(self, currentyear, oneyear, twoyears, threeyears):
        self.currentyearDF = pd.read_csv(currentyear)
        self.oneyearDF = pd.read_csv(oneyear)
        self.twoyearDF = pd.read_csv(twoyears)
        self.threeyearDF = pd.read_csv(threeyears)
