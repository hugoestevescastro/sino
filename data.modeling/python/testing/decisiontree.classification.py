import data
import helper as h
from sklearn import tree

#data.classification()

train = h.get_data('../files/output/classification.data.csv')
test = h.get_data('../files/output/test.csv')
#train = train.drop(columns=['Weekly_Sales'])
#test = test.drop(columns=['Weekly_Sales'])

# The columns that we will be making predictions with.
x_columns = ['Store', 'Dept', 'week_number', 'IsHoliday', 'Type',
             'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# The column that we want to predict.
y_column = ["class"]

clf = tree.DecisionTreeClassifier()
clf.fit(X=train[x_columns], y=train[y_column].values.ravel())
clf.feature_importances_

predictions = clf.predict(test[x_columns])
test['class'] = predictions

test.to_csv('../files/output/decisionTree.predictions.csv')

print(test['class'].value_counts())
