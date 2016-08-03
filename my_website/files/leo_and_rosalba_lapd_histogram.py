

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('crimes_2012_2015.csv', quoting=2)['TIME.OCC']
data.hist(bins=24)

plt.xlim([0,2330])
plt.title("Time of Crimes as Reported by LAPD (2012-2015)")
plt.xlabel("Time (in military time)")
plt.ylabel("Number of Crimes Reported")

plt.show()