import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./csv/output/data.csv')

x = np.asarray(data["Store"].tolist())
y = np.asarray(data["Weekly_Sales"].tolist())

plt.scatter(x, y, s=0.5, label="label", color="red")
plt.show()
