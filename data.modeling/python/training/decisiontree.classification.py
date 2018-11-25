import data
import helper as h
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

#data.classification()

df = h.get_data('../files/output/classification.data.csv')

X = df.drop(columns=['class'])
y = df['class'].values

# Split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 100)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

print("finished")
classe_names = str(classifier.classes_)
cols = X.columns
export_graphviz(classifier, out_file='../files/output/decisiontree.dot', feature_names=cols)


#print(feature_names)
#export_graphviz(classifier, out_file='tree.dot', feature_names=cols, class_names=classe_names)
print("1")

#dot_data = StringIO()
#print("2")
#export_graphviz(classifier, out_file=dot_data,filled=True, rounded=True, special_characters=True, featurenames=predictor)
#print("3")
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#print("4")
#Image(graph.create_png())
#print("5")

