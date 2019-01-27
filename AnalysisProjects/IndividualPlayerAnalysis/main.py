import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#The template for each of the scatter plots is the sameself.
#I plot the scatter plots, and set the axis labels and titlesself.
#After that, I just save the scatter plot to a file
#For this project, I used 2018 statistics

df = pd.read_csv("data.csv");

fig, ax = plt.subplots();

#HR vs. SLG scatter plot
HRvsSLGScatter = ax.scatter(df['HR'], df['SLG'])

ax.set_xlabel("HRs in 2018")
ax.set_ylabel("SLG in 2018")
ax.set_title("HR vs. SLG")

ax.set_xlim([0, None])
ax.set_ylim([0, None])

plt.savefig('HRvsSLG.png')

ax.clear()

#H vs. AVG scatter plot
HRvsAVGScatter = ax.scatter(df['H'], df['BA'])

ax.set_xlabel("H in 2018")
ax.set_ylabel("AVG. in 2018")
ax.set_title("H vs. AVG.")

ax.set_xlim([0, None])
ax.set_ylim([0, None])

plt.savefig('HvsAVG.png')

ax.clear()

#Average OPS Per Age
meanOPS = df.groupby('Age')['OPS'].mean()
meanOPS = meanOPS.reset_index()

AgevsAverageOPS = ax.scatter(meanOPS['Age'], meanOPS['OPS'])

ax.set_xlabel("Age")
ax.set_ylabel("Average OPS")
ax.set_title("Age vs. Average OPS")

plt.savefig('AgevsAverageOPS')

ax.clear()

#Average OPS Per Age
meanSO = df.groupby('Age')['SO'].mean()
meanSO = meanSO.reset_index()

AgevsAverageSO = ax.scatter(meanSO['Age'], meanSO['SO'])

ax.set_xlabel("Age")
ax.set_ylabel("Average SO")
ax.set_title("Age vs. Average SO")

plt.savefig('AgevsAverageSO')

ax.clear()
