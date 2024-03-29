# -*- coding: utf-8 -*-
"""ProjectUrbanFarming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YPSGBzdy_OY6w7_yGF6_OOXmrzeGHz_M
"""

import pandas as pd
import io

df = pd.read_csv('/content/DataSet.csv.txt',parse_dates=True)

from google.colab import drive
drive.mount('/content/drive')

df

X = df.iloc[:, :9]
y= df.iloc[:, [9]]
X = X.to_numpy()
y = y.to_numpy()

df.isnull()

df.isnull().sum()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=9)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Accuracy:", accuracy)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

y_pred = knn.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
import string

classes = ['lentil','Tomatoes','Carrot','Radish','Bean','Cucumber','Lemon','Pomegranate','Papaya','Coconut','Rose','Green Chilli']


cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='g', xticklabels=classes, yticklabels=classes)
plt.xlabel('Predicted Labels', fontsize=20)
plt.ylabel('True Labels', fontsize=20)
plt.title('Confusion Matrix', fontsize=35)
plt.show()

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
acc=accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred,average='macro')
precision = precision_score(y_test, y_pred,average='macro')
f1_score = f1_score(y_test, y_pred,average='macro')

print("Accuracy   %.4f"%(acc*100),"%")
print("RECALL     %.4f"%(recall*100),"%")
print("Precision  %.4f"%(precision*100),"%")
print("F1-Score   %.4f"%(f1_score*100),"%")

print(X.shape)
print(y.shape)

if X.shape[0] != y.shape[0]:
  print("X and y rows are mismatched, check dataset again")

import pandas as pd
import io
import numpy as np
df = pd.read_csv('/content/Final.csv',parse_dates=True)
X = df.iloc[:, :9]
y= df.iloc[:, [9]]
X = X.to_numpy()
y = y.to_numpy()
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
df1 = pd.read_csv('/content/datafinal.csv',parse_dates=True)
n=float(df1.loc[:,"Ni"])
p=float(df1.loc[:,"P"])
k=float(df1.loc[:,"K"])
shum=float(df1.loc[:,"SH"])
stemp=float(df1.loc[:,"ST"])
ahum=float(df1.loc[:,"AH"])
atemp=float(df1.loc[:,"AT"])
ph=float(df1.loc[:,"PH"])
rf=float(df1.loc[:,"Rainfall"])
p=[n,p,k,shum,stemp,ahum,atemp,ph,rf]
l=[]
for i in range(1,100):
  knn = KNeighborsClassifier(n_neighbors=i*5)
  knn.fit(X_train, y_train)
  y_pred = knn.predict([p])
  if y_pred not in l:
    l.append(y_pred)

for i in l:
  print(i)

import geocoder

# Get the current location based on public IP address
location = geocoder.ip('me')

if location:
    latitude = location.latlng[0]
    longitude = location.latlng[1]
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
else:
    print('Failed to retrieve location data.')

import geocoder

# Get the current location based on public IP address
location = geocoder.ip('me')

if location:
    lat = location.latlng[0]
    lon = location.latlng[1]

else:
    print('Failed to retrieve location data.')

import requests
import json

API_KEY = '1985d4d0a323cec96f0ab250186325ac'



url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

response = requests.get(url)
data = json.loads(response.text)

Hum = data['main']['humidity']
print(Hum)