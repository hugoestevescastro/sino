import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=> READING DATA. PLEASE WAIT...")
data = pd.read_csv('./csv/output/data.csv')

# As for KNN Regression, y values are always the value
# we want to predict, so y=Weekly_Sales
# X values are variable, so in this case x=Store

x = np.asarray(data["Store"].tolist())
y = np.asarray(data["Weekly_Sales"].tolist())

plt.scatter(x, y, s=5, label="label", color="green")
plt.show()
