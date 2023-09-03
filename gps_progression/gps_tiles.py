import pandas as pd
import numpy as np


bottomLeft = (39.77750000, 116.17944444)
bottomRight = (39.77750000, 116.58888889)
topLeft = (40.04722222, 116.58888889)
topRight = (40.04722222, 116.17944444)

df = pd.read_csv('D:\Kuch banara hu\ecs\gps_progression\gps_progression.csv')

cols = np.linspace(bottomLeft[1], bottomRight[1], num=18)
rows = np.linspace(bottomLeft[0], topLeft[0], num=15)

print(cols)
print(rows)

# df['col'] = np.searchsorted(cols, df['long'])
# df['row'] = np.searchsorted(rows, df['lat'])
