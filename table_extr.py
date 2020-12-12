import requests
import pandas as pd
import tables

for i in range(0,len(tables.quali2019)):
    url = tables.quali2019[i]
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    print(df)
    name = 'quali_' + str(i) + '_2019.csv'
    df.to_csv(name)
url = tables.race2019
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
name = 'race_2019.csv'
df.to_csv(name)

for i in range(0,len(tables.quali2018)):
    url = tables.quali2018[i]
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    print(df)
    name = 'quali_' + str(i) + '_2018.csv'
    df.to_csv(name)
url = tables.race2018
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
name = 'race_2018.csv'
df.to_csv(name)

for i in range(0,len(tables.quali2017)):
    url = tables.quali2017[i]
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    print(df)
    name = 'quali_' + str(i) + '_2017.csv'
    df.to_csv(name)
url = tables.race2017
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
name = 'race_2017.csv'
df.to_csv(name)

for i in range(0,len(tables.quali2016)):
    url = tables.quali2016[i]
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    print(df)
    name = 'quali_' + str(i) + '_2016.csv'
    df.to_csv(name)
url = tables.race2016
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
name = 'race_2016.csv'
df.to_csv(name)