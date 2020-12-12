#Para excluir colunas inúteis

import pandas as pd
import os
import glob

#Percorre o diretório atual em busca dos arquivos .csv
current = os.getcwd()
os.chdir(current)
result = glob.glob('*.{}'.format('csv'))

#RPara remover as colunas, é necessário fazer da primeira linha, o cabeçalho
for file in result:
    #transforma em Dataframe
    df = pd.read_csv(file)
    #Exclui as colunas Team e Drivers
    df.drop('Drivers',axis=1,inplace=True)
    df.to_csv(file, sep=',')
    df.head()
