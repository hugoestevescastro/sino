import data
import helper as h
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import math

#data.classification()

df = h.get_data('./files/output/classification.data.csv')

X = df.drop(columns=['class'])
y = df['class'].values

# Split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

# Create the knn classifier model
knn = KNeighborsClassifier(n_neighbors=int(math.sqrt(len(df))))

# Fit the classifier into the data
knn.fit(X_train, y_train)

# Predict values for test data
predictions = knn.predict(X_test)

# Test the model accuracy
accuracy = knn.score(X_test, y_test)

print("The KNN Classifier model have " + str(int(accuracy * 100)) + " of accuracy.")


