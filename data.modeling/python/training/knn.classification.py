import data
import helper as h
from sklearn.metrics import classification_report, confusion_matrix, \
                            accuracy_score, precision_score, f1_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
# Adição das classes mediante o volume de vendas
#data.classification()

# Criação do data frame a partir do ficheiro csv
df = h.get_data('../files/output/classification.data.csv')

# Criação de data frame com base no data frame train,
# sem a coluna 'Weekly_Sales', visto que é o valor que se pretende prever
X = df.drop(columns=['class', 'Unnamed: 0', 'Dept', 'Type', 'Size'])

# Criação de uma lista com os valores da coluna que se pretende prever
y = df['class'].values.tolist()
# Utilização de um módulo da sklearn para dividir o
# data frame train, em train e test, por forma a avaliar a accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Obtenção do melhor valor de K
acc_arr = []
predict_arr = []
conf_matrix = []
class_report = []
prec_score = []
f1 = []
recall = []
for K in range(25):
    print(str(K) + " - Running . . .")
    K_value = K+1
    # Criação do modelo com K_value vizinhos
    neigh = KNeighborsClassifier(n_neighbors=K_value, weights='uniform', algorithm='auto')
    # Preenchimento do modelo com o data frame de train
    neigh.fit(X_train, y_train)
    # Obtenção de previsões
    y_pred = neigh.predict(X_test)
    predict_arr.append(y_pred)

    # Cálculo de métricas
    acc_arr.append(accuracy_score(y_test, y_pred)*100)
    conf_matrix.append(confusion_matrix(y_test, y_pred))
    class_report.append(classification_report(y_test, y_pred))
    prec_score.append(precision_score(y_test, y_pred, average='micro')*100)
    f1.append(f1_score(y_test, y_pred, average='micro')*100)
    recall.append(recall_score(y_test, y_pred, average='micro')*100)

highest_score = acc_arr.index(max(acc_arr))
# Apresentação da confusion_matrix
print(conf_matrix[highest_score])
# Apresentação do classification report
print(class_report[highest_score])
print("Accuracy: " + str(acc_arr[highest_score]))
print("Precision: " + str(prec_score[highest_score]))
print("F1: " + str(f1[highest_score]))
print("Recall: " + str(recall[highest_score]))
