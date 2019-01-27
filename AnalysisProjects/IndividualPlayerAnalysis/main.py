import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv");

plt.plot(df['HR'],df['OPS'])
plt.save('HRvsOPS.png')

print(df);
