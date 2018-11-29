import data
import helper as h
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, \
    accuracy_score, recall_score, precision_score, f1_score
from sklearn.tree import export_graphviz

#data.classification()

df = h.get_data('../files/output/classification.data.csv')

X = df.drop(columns=['class', 'Unnamed: 0', 'Dept'])
y = df['class'].values

# Utilização de um módulo da sklearn para dividir o
# data frame train, em train e test, por forma a avaliar a accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)

# Criação do modelo de classificação, Decision tree
classifier = DecisionTreeClassifier()

# Preenchimento do modelo com o data frame de treino
classifier.fit(X_train, y_train)

# Obtenção das previsões de acordo com dados de teste
y_pred = classifier.predict(X_test)

# Apresentação da confusion_matrix
print(confusion_matrix(y_test, y_pred))

# Apresentação do classification report
print(classification_report(y_test, y_pred))

# Apresentação das métricas de performance do modelo
print("accuracy_score: " + str(accuracy_score(y_test, y_pred) * 100) + "%")
print("recall_score: " + str(recall_score(y_test, y_pred, average='micro') * 100) + "%")
print("precision_score: " + str(precision_score(y_test, y_pred, average='micro') * 100) + "%")
print("f1_score: " + str(f1_score(y_test, y_pred, average='micro') * 100) + "%")

# Criação do ficheiro .dot para gerar gráficos
export_graphviz(classifier, out_file='../files/output/decisiontree.classification.dot', feature_names=X.columns)