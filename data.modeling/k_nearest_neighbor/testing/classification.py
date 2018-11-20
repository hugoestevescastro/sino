import data
import helper as h
from sklearn.neighbors import KNeighborsClassifier
import math

data.classification()

train = h.get_data('./files/output/classification.data.csv')
test = h.get_data('./files/output/test.csv')

# The columns that we will be making predictions with.
x_columns = ['Store', 'Dept', 'week_number', 'IsHoliday', 'Type',
             'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# The column that we want to predict.
y_column = ["class"]

# Create the knn model. Look at the sqrt(len(test)) closest neighbor
knn = KNeighborsClassifier(n_neighbors=int(math.sqrt(len(test))))

# Fit the model on the training data.
knn.fit(train[x_columns], train[y_column].values.ravel())

# Make point predictions on the test set using the fit model.
predictions = knn.predict(test[x_columns])

# Add predictions of Weekly_Sales to the test set
test['class'] = predictions

# Export to *.csv
test.to_csv('./files/output/classification.predictions.csv')
