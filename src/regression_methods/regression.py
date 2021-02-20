import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("src/priceData.csv")
px = data.iloc[:, 1:]
px = px.interpolate()

logpx = np.log(px)
logpx.rolling(252).mean().plot()
plt.show()
