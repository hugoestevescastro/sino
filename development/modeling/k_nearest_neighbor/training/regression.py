from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import helper as h
import data
import math

# Preparing the data
#data.treatment()

# Get train and test set
train = h.get_data('./csv/output/regression.data.csv')

# The columns that we will be making predictions with.
X = train.drop(columns=['Weekly_Sales'])

# The column that we want to predict.
y = train["Weekly_Sales"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create the knn model. Look at the sqrt(len(test)) closest neighbor
knn = KNeighborsRegressor(n_neighbors=int(math.sqrt(len(train))))

# Fit the model on the training data.
knn.fit(X_train, y_train)

# Make point predictions on the test set using the fit model.
predictions = knn.predict(X_test)

accuracy = knn.score(X_test, y_test)

print("The KNN Regressor model have " + str(int(accuracy * 100)) + " of accuracy.")
