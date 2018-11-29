from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import helper as h
from math import sqrt
import data

# Preparação dos dados
#data.treatment()

# Criação de data frames a partir de ficheiros csv
train = h.get_data('../files/output/regression.data.csv')

# Criação de data frame com base no data frame train,
# sem a coluna 'Weekly_Sales', visto que é o valor que
# se pretende prever
X = train.drop(columns=['Weekly_Sales'])

# Criação de uma lista com os valores da coluna que se
# pretende prever
y = train["Weekly_Sales"].values

# Utilização de um módulo da sklearn para dividir o
# data frame train, em train e test, por forma a avaliar a accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Obtenção do melhor valor de K
acc_arr = []
predict_arr = []
for K_value in range(2, 10):
    # Criação do modelo com K_value vizinhos
    knn = KNeighborsRegressor(n_neighbors=K_value)

    # Preenchimento do modelo com o data frame de train
    knn.fit(X_train, y_train)

    # Obtenção de previsões
    predictions = knn.predict(X_test)

    # Cálculo da accuracy do modelo com K_value vizinhos
    mse = mean_squared_error(y_train, predictions, multioutput='uniform_average')
    rmse = sqrt(mse)
    mae = mean_absolute_error(y_train, predictions, multioutput='uniform_average')
    print('******* K = ' + str(K_value) + ' **********')
    print("Mean squared error: ", mse)
    print("Root mean squared error: ", rmse)
    print("Mean absolute error is ", mae)
    print('\n')
