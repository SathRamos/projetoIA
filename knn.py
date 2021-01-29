import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#algoritmo 1-nn
# Importa o  dataset
dataset = pd.read_csv('data_set.csv')
dataset = dataset.dropna()
X = dataset.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]].values
y = dataset.iloc[:, -1].values

print("variaveis independentes")
print(X)
print("variaveis dependentes")
print(y)

# Divide o dataset em um conjunto de treino e um de teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Codificar caracteres do dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Treina o modelo k-nn no conjunto de treino
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Prediz o resultado dos conjuntos de teste
y_pred = classifier.predict(X_test)

# Constroi a matriz de confusão
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)

print(ac)