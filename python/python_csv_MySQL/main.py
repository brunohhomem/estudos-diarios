import pandas as pd


def lerCSV():
    arquivoCSV = pd.read_csv('dados.csv', index_col=False, delimiter=',')
    arquivoCSV.head()
    return arquivoCSV


print(lerCSV())
