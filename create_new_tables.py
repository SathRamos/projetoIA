import pandas as pd
import os
import glob
import csv

current = os.getcwd()
os.chdir(current)

#Cria as novas tabelas
with open('new_tables/lmp1_2016.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp1_2017.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp1_2018.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp1_2019.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp2_2016.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp2_2017.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp2_2018.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/lmp2_2019.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gtePro_2016.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gtePro_2017.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gtePro_2018.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gtePro_2019.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gteAm_2016.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gteAm_2017.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gteAm_2018.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])

with open('new_tables/gteAm_2019.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['id', 'posQuali_0', 'posQuali_1', 'posQuali_2', 'posQuali_3',
                         'lapsQuali_0', 'lapsQuali_1', 'lapsQuali_2', 'lapsQuali_3', 
                         'timeQuali_0', 'timeQuali_1', 'timeQuali_2', 'timeQuali_3', 
                         'kphQuali_0', 'kphQuali_1', 'kphQuali_2', 'kphQuali_3', 'posRace'])