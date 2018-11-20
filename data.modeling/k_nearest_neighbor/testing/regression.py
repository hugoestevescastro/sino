from sklearn.neighbors import KNeighborsRegressor
import helper as h
import data
import math

# Preparing the data
# data.treatment()

# Get train and test set
train = h.get_data('./files/output/regression.data.csv')
test = h.get_data('./files/output/test.csv')

# The columns that we will be making predictions with.
x_columns = ['Store', 'Dept', 'week_number', 'IsHoliday', 'Type',
             'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# The column that we want to predict.
y_column = ["Weekly_Sales"]

# Create the knn model. Look at the sqrt(len(test)) closest neighbor
knn = KNeighborsRegressor(n_neighbors=int(math.sqrt(len(test))))

# Fit the model on the training data.
knn.fit(train[x_columns], train[y_column])

# Make point predictions on the test set using the fit model.
predictions = knn.predict(test[x_columns])

# Add predictions of Weekly_Sales to the test set
test['Weekly_Sales'] = predictions

# Export to *.csv
test.to_csv('./files/output/regression.predictions.csv')
