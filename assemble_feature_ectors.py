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

lmp1_2016 = np.empty((0,18), str)
lmp1_2017 = np.empty((0,18), str)
lmp1_2018 = np.empty((0,18), str)
lmp1_2019 = np.empty((0,18), str)
lmp2_2016 = np.empty((0,18), str)
lmp2_2017 = np.empty((0,18), str)
lmp2_2018 = np.empty((0,18), str)
lmp2_2019 = np.empty((0,18), str)
gtePro_2016 = np.empty((0,18), str)
gtePro_2017 = np.empty((0,18), str)
gtePro_2018 = np.empty((0,18), str)
gtePro_2019 = np.empty((0,18), str)
gteAm_2016 = np.empty((0,18), str)
gteAm_2017 = np.empty((0,18), str)
gteAm_2018 = np.empty((0,18), str)
gteAm_2019 = np.empty((0,18), str)

firstLine = np.array(['id', 'pos_quali_0', 'pos_quali_1', 'pos_quali_2', 'pos_quali_3',
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
        itemLaps = row.loc["Laps"]
        itemTime = row.loc["Time"]
        itemKph = row.loc["Kph"]

        #print(itemClass)

        if year == "2016":
            if itemClass == "LMP1":
                print("check LMP1")
                if itemNum not in lmp1_2016[:,0]:
                        lmp1_2016 = np.append(lmp1_2016, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(lmp1_2016[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp1_2016[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp1_2016[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp1_2016[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp1_2016[y_coord, x_coord] = itemKph
                
            elif itemClass == "LMP2":
                print("check LMP2")
                if itemNum not in lmp2_2016[:,0]:
                        lmp2_2016 = np.append(lmp2_2016, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(lmp2_2016[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp2_2016[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp2_2016[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp2_2016[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp2_2016[y_coord, x_coord] = itemKph

            elif itemClass == "GTE_Pro":
                print("check GTE_Pro")
                if itemNum not in gtePro_2016[:,0]:
                        gtePro_2016 = np.append(gtePro_2016, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gtePro_2016[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gtePro_2016[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gtePro_2016[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gtePro_2016[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gtePro_2016[y_coord, x_coord] = itemKph

            elif itemClass == "GTE_Am":
                print("check GTE_Am")
                if itemNum not in gteAm_2016[:,0]:
                        gteAm_2016 = np.append(gteAm_2016, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gteAm_2016[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gteAm_2016[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gteAm_2016[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gteAm_2016[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gteAm_2016[y_coord, x_coord] = itemKph
        
        elif year == "2017":
            if itemClass == "LMP1":
                if itemNum not in lmp1_2017[:,0]:
                        lmp1_2017 = np.append(lmp1_2017, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)
        
                y_coord = np.where(lmp1_2017[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp1_2017[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp1_2017[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp1_2017[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp1_2017[y_coord, x_coord] = itemKph
                
            elif itemClass == "LMP2":
                if itemNum not in lmp2_2017[:,0]:
                        lmp2_2017 = np.append(lmp2_2017, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(lmp2_2017[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp2_2017[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp2_2017[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp2_2017[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp2_2017[y_coord, x_coord] = itemKph  

            elif itemClass == "GTE_Pro":
                if itemNum not in gtePro_2017[:,0]:
                        gtePro_2017 = np.append(gtePro_2017, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gtePro_2017[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gtePro_2017[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gtePro_2017[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gtePro_2017[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gtePro_2017[y_coord, x_coord] = itemKph  

            elif itemClass == "GTE_Am":
                if itemNum not in gteAm_2017[:,0]:
                        gteAm_2017 = np.append(gteAm_2017, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gteAm_2017[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gteAm_2017[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gteAm_2017[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gteAm_2017[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gteAm_2017[y_coord, x_coord] = itemKph  

        elif year == "2018":
            if itemClass == "LMP1":
                if itemNum not in lmp1_2018[:,0]:
                        print("***Added new row***")
                        print(itemNum)
                        lmp1_2018 = np.append(lmp1_2018, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)
                        dataframe = pd.DataFrame(lmp1_2018)
                        print(dataframe)

                #print("***Insert pos in existing row***")
                #print(itemNum)
                y_coord = np.where(lmp1_2018[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                #print(x_coord)
                #print(y_coord)
                lmp1_2018[y_coord, x_coord] = itemPos
                dataframe = pd.DataFrame(lmp1_2018)
                #print(dataframe)

                #print("***Insert laps in existing row***")
                #print(itemNum)
                x_coord = np.where(firstLine == "laps_"+event)
                #print(x_coord)
                #print(y_coord)
                lmp1_2018[y_coord, x_coord] = itemLaps
                dataframe = pd.DataFrame(lmp1_2018)
                #print(dataframe)

                #print("***Insert time in existing row***")
                #print(itemNum)
                x_coord = np.where(firstLine == "time_"+event)
                #print(x_coord)
                #print(y_coord)
                lmp1_2018[y_coord, x_coord] = itemTime
                dataframe = pd.DataFrame(lmp1_2018)
                #print(dataframe)

                #print("***Insert kph in existing row***")
                #print(itemNum)
                x_coord = np.where(firstLine == "kph_"+event)
                #print(x_coord)
                #print(y_coord)
                lmp1_2018[y_coord, x_coord] = itemKph
                dataframe = pd.DataFrame(lmp1_2018)
                #print(dataframe)
                
            elif itemClass == "LMP2":
                if itemNum not in lmp2_2018[:,0]:
                        lmp2_2018 = np.append(lmp2_2018, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(lmp2_2018[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp2_2018[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp2_2018[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp2_2018[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp2_2018[y_coord, x_coord] = itemKph  

            elif itemClass == "GTE_Pro":
                if itemNum not in gtePro_2018[:,0]:
                        gtePro_2018 = np.append(gtePro_2018, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gtePro_2018[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gtePro_2018[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gtePro_2018[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gtePro_2018[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gtePro_2018[y_coord, x_coord] = itemKph    

            elif itemClass == "GTE_Am":
                if itemNum not in gteAm_2018[:,0]:
                        gteAm_2018 = np.append(gteAm_2018, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gteAm_2018[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gteAm_2018[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gteAm_2018[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gteAm_2018[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gteAm_2018[y_coord, x_coord] = itemKph      
        
        elif year == "2019":
            if itemClass == "LMP1":
                if itemNum not in lmp1_2019[:,0]:
                        lmp1_2019 = np.append(lmp1_2019, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(lmp1_2019[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp1_2019[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp1_2019[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp1_2019[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp1_2019[y_coord, x_coord] = itemKph      
                
            elif itemClass == "LMP2":
                if itemNum not in lmp2_2019[:,0]:
                        lmp2_2019 = np.append(lmp2_2019, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)
                
                y_coord = np.where(lmp2_2019[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                lmp2_2019[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                lmp2_2019[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                lmp2_2019[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                lmp2_2019[y_coord, x_coord] = itemKph  

            elif itemClass == "GTE_Pro":
                if itemNum not in gtePro_2019[:,0]:
                        gtePro_2019 = np.append(gtePro_2019, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)
                
                y_coord = np.where(gtePro_2019[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gtePro_2019[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gtePro_2019[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gtePro_2019[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gtePro_2019[y_coord, x_coord] = itemKph  

            elif itemClass == "GTE_Am":
                if itemNum not in gteAm_2019[:,0]:
                        gteAm_2019 = np.append(gteAm_2019, np.array([[itemNum, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]], dtype=object), axis=0)

                y_coord = np.where(gteAm_2019[:,0] == itemNum)
                x_coord = np.where(firstLine == "pos_"+event)
                gteAm_2019[y_coord, x_coord] = itemPos

                x_coord = np.where(firstLine == "laps_"+event)
                gteAm_2019[y_coord, x_coord] = itemLaps

                x_coord = np.where(firstLine == "time_"+event)
                gteAm_2019[y_coord, x_coord] = itemTime

                x_coord = np.where(firstLine == "kph_"+event)
                gteAm_2019[y_coord, x_coord] = itemKph  

df = pd.DataFrame(lmp2_2017)
print(df)


df = pd.DataFrame(lmp1_2016)
df.to_csv('new_tables/lmp1_2016.csv', index=True)
df = pd.DataFrame(lmp1_2017)
df.to_csv('new_tables/lmp1_2017.csv', index=True)
df = pd.DataFrame(lmp1_2018)
df.to_csv('new_tables/lmp1_2018.csv', index=True)
df = pd.DataFrame(lmp1_2019)
df.to_csv('new_tables/lmp1_2019.csv', index=True)
df = pd.DataFrame(lmp2_2016)
df.to_csv('new_tables/lmp2_2016.csv', index=True)
df = pd.DataFrame(lmp2_2017)
df.to_csv('new_tables/lmp2_2017.csv', index=True)
df = pd.DataFrame(lmp2_2018)
df.to_csv('new_tables/lmp2_2018.csv', index=True)
df = pd.DataFrame(lmp2_2019)
df.to_csv('new_tables/lmp2_2019.csv', index=True)
df = pd.DataFrame(gtePro_2016)
df.to_csv('new_tables/gtePro_2016.csv', index=True)
df = pd.DataFrame(gtePro_2017)
df.to_csv('new_tables/gtePro_2017.csv', index=True)
df = pd.DataFrame(gtePro_2018)
df.to_csv('new_tables/gtePro_2018.csv', index=True)
df = pd.DataFrame(gtePro_2019)
df.to_csv('new_tables/gtePro_2019.csv', index=True)
df = pd.DataFrame(gteAm_2016)
df.to_csv('new_tables/gteAm_2016.csv', index=True)
df = pd.DataFrame(gteAm_2017)
df.to_csv('new_tables/gteAm_2017.csv', index=True)
df = pd.DataFrame(gteAm_2018)
df.to_csv('new_tables/gteAm_2018.csv', index=True)
df = pd.DataFrame(gteAm_2019)
df.to_csv('new_tables/gteAm_2019.csv', index=True)