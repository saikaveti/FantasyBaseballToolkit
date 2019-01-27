import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv");

fig, ax = plt.subplots();

HRvsOPSScatter = ax.scatter(df['HR'], df['OPS'])

ax.set_xlabel("HRs in 2018")
ax.set_ylabel("OPS in 2018")
ax.set_title("HR vs. OPS")

plt.savefig('HRvsOPS.png')

ax.clear()

HRvsAVGScatter = ax.scatter(df['HR'], df['BA'])

ax.set_xlabel("HRs in 2018")
ax.set_ylabel("AVG. in 2018")
ax.set_title("HR vs. AVG.")

plt.savefig('HRvsAVG.png')
