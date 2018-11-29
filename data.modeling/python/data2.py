import helper as h
import pandas as pd
import numpy as np


def treatment(path_to='./files/input/'):
    # Criação de data frames através de ficheiros csv
    _features = h.get_data(path_to + 'features.csv')


    # Substitui valores com strings vazias por valores NaN
    _data = _features.replace('', np.nan)

    # Exportação dos data frames para ficheiros .csv
    _data.to_csv('./files/output/regression.features.csv')

def run():

    _features = h.get_data('./files/output/knn.regression.predictions.csv')
    print(_features.shape)