import pandas as pd
import os
import glob
import csv
import numpy as np

#Percorre o diretório atual em busca dos arquivos .csv
current = os.getcwd()
os.chdir(current)

current = os.getcwd()
os.chdir(current)
result = glob.glob('*.{}'.format('csv'))

dataSet = np.empty((0,18), str)

firstLine = np.array(['id', 'class' 'pos_quali_0', 'pos_quali_1', 'pos_quali_2', 'pos_quali_3',
                                'laps_quali_0', 'laps_quali_1', 'laps_quali_2', 'laps_quali_3', 
                                'time_quali_0', 'time_quali_1', 'time_quali_2', 'time_quali_3', 
                                'kph_quali_0', 'kph_quali_1', 'kph_quali_2', 'kph_quali_3', 'pos_race'], dtype=object)

for table in result:
    df = pd.read_csv(table)
    year = event = table
    year = year[-8:-4]
    event = event[0:-9]
    print("Event: ", event)
    print("Year: ", year)
    del(df['Unnamed: 0'])
    del(df['Unnamed: 0.1'])
    del(df['Unnamed: 0.1.1'])
    del(df['Gap'])
    del(df['Interval'])
    del(df['Best'])
    del(df['Lap'])

    numRows = df.shape[0]
    for i in range(0, numRows):
        row = df.iloc[i]
        itemPos = row.loc["Pos"]
        itemNum = row.loc["No"]
        itemClass = row.loc["Class"]
        itemClass = itemClass.replace(" ", "_")
        itemClass = itemClass.lower()
        itemLaps = row.loc["Laps"]
        itemTime = str(row.loc["Time"])
        itemTime = itemTime[:-4]
        itemTime = itemTime.replace(":", ".")
        itemKph = "{:.3f}".format(row.loc["Kph"])

        #define categorias por número
        if itemClass == "lmp1-h": itemClass = 0
        elif itemClass == "lmp1": itemClass = 1
        elif itemClass == "lmp2": itemClass = 2
        elif itemClass == "gte_pro": itemClass = 3
        elif itemClass == "gte_am": itemClass = 4

        if itemNum not in dataSet[:,0]:
                dataSet = np.append(dataSet, np.array([[itemNum, itemClass, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)
        
        y_coord = np.where(dataSet[:,0] == itemNum)
        x_coord = np.where(firstLine == "pos_"+event)
        dataSet[y_coord, x_coord] = itemPos

        x_coord = np.where(firstLine == "laps_"+event)
        dataSet[y_coord, x_coord] = itemLaps

        x_coord = np.where(firstLine == "time_"+event)
        dataSet[y_coord, x_coord] = itemTime

        x_coord = np.where(firstLine == "kph_"+event)
        dataSet[y_coord, x_coord] = itemKph
        
                
df = pd.DataFrame(dataSet)
print(df)


df = pd.DataFrame(dataSet)
df.to_csv('data_set.csv', index=True)

#transforma o DNF em 100 (significa que terminou numa posição acima dos outros)
numRows = df.shape[0]

if 'DNF' in df.values:
    df = df.replace(['DNF', "NC", "DSQ"],'100')

#remove linhas com dados faltando (NaN)
df = df.dropna()
print("***apos remocao de NaN")

#del df['Unnamed: 0']

print(df)

df.to_csv('data_set.csv', index=True)