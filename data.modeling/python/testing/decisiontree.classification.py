import data
import helper as h
from sklearn import tree
from sklearn.preprocessing import Imputer

data.classification()

train = h.get_data('../files/output/classification.data.csv')
test = h.get_data('../files/output/test.csv')

# The columns that we will be making predictions with.
x_columns = ['Store', 'Dept', 'week_number', 'IsHoliday', 'Type',
             'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# The column that we want to predict.
y_column = ["class"]

# Troca os valores nulos que interromperiam o modelo, pela média
# Esta estratégia foi adotada devido ao facto de se tratar das colunas Unemployment e CPI
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(test[x_columns])
X_test_imp = imp.transform(test[x_columns])


clf = tree.DecisionTreeClassifier()
clf.fit(X=train[x_columns], y=train[y_column].values.ravel())
clf.feature_importances_

predictions = clf.predict(X_test_imp)
test['class'] = predictions

test.to_csv('../files/output/decisionTree.predictions.csv')
