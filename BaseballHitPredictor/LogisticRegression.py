import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class Classifier:

    def __init__(self, file_read):
        self.data = pd.read_csv(file_read)


    def perform_regression(self):
        self.data.head()

        self.data.drop(["AB", "IBB", "TA", "HBP", "3B", "HR", "OBP", "2B", "OPS", "ISO", "SECA", "RC27", "RC", "TB", "CS", "GIDP", "SF"], axis = 1, inplace = True)

        print(self.data.info())

        X = self.data.ix[:,(0,1,2,3,4,5)].values
        y = self.data.ix[:,6].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .25, random_state=25)

        LogReg = LogisticRegression()
        LogReg.fit(X_train, y_train)

        y_pred = LogReg.predict(X_test)

        matrix = confusion_matrix(y_test, y_pred)
        print(matrix)
        print(classification_report(y_test, y_pred))
        #with pd.option_context('display.max_rows', None, 'display.max_columns', 24):
            #print(self.data)
