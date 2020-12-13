import pandas as pd
import os
import glob

#Percorre o diretório atual em busca dos arquivos .csv
current = os.getcwd()
os.chdir(current)
result = glob.glob('*.{}'.format('csv'))
print("Tables:")
print(result)

key=0
while key == 0:
    name = input("Type a table name to see it (ex: table.csv)\nType q to exit\n")
    if name == 'q':
        key = 1
    else:
        if name in result:
            #transforma em Dataframe
            df = pd.read_csv(name)
            print(df)
    
