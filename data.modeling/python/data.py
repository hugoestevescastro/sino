import helper as h
import numpy as np


def treatment(path_to='../files/input/'):
    # Criação de data frames através de ficheiros csv
    _train = h.get_data(path_to + 'train.csv')
    _features = h.get_data(path_to + 'features.csv')
    _stores = h.get_data(path_to + 'stores.csv')
    _test = h.get_data(path_to + 'test.csv')

    # Substituição do tipo de loja por valores númerico
    # de forma a não existir conflitos nos algoritmos de classificação
    _stores['Type'] = _stores['Type'].map({'A': 0, 'B': 1, 'C': 2})

    # Junção de data frames por forma a ter um contendo todos os dados
    _data = h.merge_data(_features, _stores, 'Store')
    _data = h.merge_data(_data, _train, ['Store', 'Date'])
    _test = h.merge_data(_features, _test, ['Store', 'Date'])
    _test = h.merge_data(_stores, _test, 'Store')

    # Correção da coluna IsHoliday (devido á junção) e correspondente conversão de booleano para númerico
    _data = _data.drop('IsHoliday_y', axis=1)
    _data = _data.rename(columns={'IsHoliday_x': 'IsHoliday'})
    _data['IsHoliday'] = _data['IsHoliday'].map({False: 0, True: 1})
    _test = _test.drop('IsHoliday_y', axis=1)
    _test = _test.rename(columns={'IsHoliday_x': 'IsHoliday'})
    _test['IsHoliday'] = _test['IsHoliday'].map({False: 0, True: 1})


    # Cálculo do número de semana do ano, e do ano, adicionando-os aos respetivos data frames
    _data['week_number'] = _data.apply(lambda row: h.calculate_week(row['Date']), axis=1)
    _data['year'] = _data.apply(lambda row: h.calculate_year(row['Date']), axis=1)
    _test['week_number'] = _test.apply(lambda row: h.calculate_week(row['Date']), axis=1)
    _test['year'] = _test.apply(lambda row: h.calculate_year(row['Date']), axis=1)

    # Drop de colunas não utilizadas
    _data = _data.drop('Date', axis=1)
    _data = _data.drop('Markdown1', axis=1)
    _data = _data.drop('Markdown2', axis=1)
    _data = _data.drop('Markdown3', axis=1)
    _data = _data.drop('Markdown4', axis=1)
    _data = _data.drop('Markdown5', axis=1)
    _test = _test.drop('Date', axis=1)
    _test = _test.drop('Markdown1', axis=1)
    _test = _test.drop('Markdown2', axis=1)
    _test = _test.drop('Markdown3', axis=1)
    _test = _test.drop('Markdown4', axis=1)
    _test = _test.drop('Markdown5', axis=1)

    # Indexação dos data frames por Store, Dept e Date
    _data.set_index(['Store', 'Dept', 'year', 'week_number'])
    _test.set_index(['Store', 'Dept', 'year', 'week_number'])

    # Substitui valores com strings vazias por valores NaN
    _data = _data.replace('', np.nan)
    _test = _test.replace('', np.nan)

    # Exportação dos data frames para ficheiros .csv
    _data.to_csv('../files/output/regression.data.csv')
    _test.to_csv('../files/output/test.csv')


def classification(path_to='./files/output/'):

    # Tratamento dos data sets fornecidos
    treatment(path_to)

    # Importação do data set
    _continuous = h.get_data(path_to + 'regression.data.csv')

    # Cálculo dos percentis com o fim de atribuir classes
    p25 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['25%']
    p50 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['50%']
    p75 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['75%']

    # Função que determina a classe de um volume de vendas com base nos percentis já calculados
    def get_class(_value):
        if _value <= p25:
            return 0
        elif p25 < _value <= p50:
            return 1
        elif p50 < _value <= p75:
            return 2
        else:
            return 3

    # Atribuição de classe de volume de vendas a cada linhas
    _continuous['class'] = _continuous.apply(lambda row: get_class(row['Weekly_Sales']), axis=1)

    # Drop da coluna Weekly Sales de forma a prevenir a previsão através deste valor
    _continuous = _continuous.drop(columns=['Weekly_Sales'])

    # Exportação dos data frames para ficheiros .csv
    _continuous.to_csv('../files/output/classification.data.csv')
