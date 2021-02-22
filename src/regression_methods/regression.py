import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# 1.1.1
data = pd.read_csv("src/priceData.csv")
print(data.dtypes)


px = data.iloc[:, 1:]
px = px.interpolate()
logpx = np.log(px)


# 1.1.2
logpx.rolling(252).mean().plot()
logpx.rolling(252).std().plot()
plt.show()

# 1.1.3
logret = logpx.diff()
logret.plot()

simpret = px.pct_change()
simpret.plot()