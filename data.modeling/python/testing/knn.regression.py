from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import Imputer
import helper as h
import data

# Preparação dos dados
data.treatment()

# Criação de data frames a partir de ficheiros csv
train = h.get_data('../files/output/regression.data.csv')
test = h.get_data('../files/output/test.csv')

# Definição das colunas a utilizar para efeitos de previsão
x_columns = ['Store', 'Dept', 'week_number', 'IsHoliday', 'Type',
             'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# Definicão da coluna que se pretende prever
y_column = ["Weekly_Sales"]

# Troca os valores nulos que interromperiam o modelo, pela média
# Esta estratégia foi adotada devido ao facto de se tratar das colunas Unemployment e CPI
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(test[x_columns])
X_test_imp = imp.transform(test[x_columns])

# Criação do modelo com o número de vizinhos calculado
# no ficheiro de treino (training/knn.regression.py)
knn = KNeighborsRegressor(n_neighbors=8)

# Preenchimento do modelo com o data frame de treino
knn.fit(train[x_columns], train[y_column])

# Obtenção das previsões de acordo com dados de teste
predictions = knn.predict(X_test_imp)

# Adição dos resultados ao data frame de teste, coluna 'class'
test['Weekly_Sales'] = predictions

# Exportação do data frame de teste para um ficheiro csv
test.to_csv('../files/output/knn.regression.predictions.csv')

