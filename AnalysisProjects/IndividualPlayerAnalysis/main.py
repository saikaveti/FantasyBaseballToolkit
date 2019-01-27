import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

#ax.set_xlim([5, None])

plt.savefig('HvsAVG.png')
