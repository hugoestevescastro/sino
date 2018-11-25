import data
import helper as h
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import math

#data.classification()

df = h.get_data('./files/output/classification.data.csv')

X = df.drop(columns=['class'])
y = df['class'].values

# Split data set into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Getting the best value of K
acc_arr = []
predict_arr = []
for K in range(25):
    K_value = K+1
    neigh = KNeighborsClassifier(n_neighbors=K_value, weights='uniform', algorithm='auto')
    neigh.fit(X_train, y_train)
    y_pred = neigh.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)*100
    acc_arr.append(accuracy)
    predict_arr.append(y_pred)
    print("Accuracy is ", accuracy, "% for K-Value:", K_value)

final_prediction = predict_arr[acc_arr.index(max(acc_arr))]

# Test the model accuracy
acc = accuracy_score(y_test, final_prediction)

print("The KNN Classifier model have " + str(int(acc * 100)) + " of accuracy.")


