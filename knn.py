import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

headerNames = np.array(['id', 'pos_quali_0', 'pos_quali_1', 'pos_quali_2', 'pos_quali_3',
                                'laps_quali_0', 'laps_quali_1', 'laps_quali_2', 'laps_quali_3', 
                                'time_quali_0', 'time_quali_1', 'time_quali_2', 'time_quali_3', 
                                'kph_quali_0', 'kph_quali_1', 'kph_quali_2', 'kph_quali_3', 'pos_race'])

for table in os.scandir('new_tables/'):
    #
    #y_coord = np.where([:,0] == "DNF")
    df = pd.read_csv(table)
    print(df)
    #transforma o DNF em 100 (significa que terminou numa posição acima dos outros)
    numRows = df.shape[0]
    #array = df.to_numpy
    #print("arrei")
    #print(array)
    if 'DNF' in df.values:
        df = df.replace(['DNF', "NC", "DSQ"],'100')
    
    print("****apos substituicao de DNF****")
    print(df)
    #remove linhas com dados faltando (NaN)
    df = df.dropna()
    print("***apos remocao de NaN")
    print(df)

#dataset = pd.read_csv("newtables/", names = headerNames)
#dataset.head()