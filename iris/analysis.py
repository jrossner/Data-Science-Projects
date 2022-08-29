import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

with open('/resources/iris.data') as raw:
    data = raw.read().splitlines()

data[0:5]

# Clean Data
sData = [obs.split(',') for obs in data]

sData[0:5]

df = pd.DataFrame(sData, columns=('sepal-length','sepal-width','petal-length','petal-width','iris'))
df.dtypes

numCols = ['sepal-length','sepal-width','petal-length','petal-width']
for col in numCols:
    df[col] = df[col].astype(float)

df.head()

# Visualize Data
for col in numCols:
    plt.hist(df[col])
    plt.title(col)
    plt.show()
    
# Split Data
dfShuff = df.sample(frac=1)
prop = .8
l = round(prop*len(df))

train = dfShuff[0:l]
test = dfShuff[l:]

# KNN

trainX = train[numCols]
trainY = train['iris']
testX = test[numCols]
testY = test['iris']

scaler = StandardScaler()
scaler.fit(trainX)

trainXS = scaler.transform(trainX)
testXS = scaler.transform(testX)

k = round(len(trainY)**.5)
model = KNeighborsClassifier(n_neighbors=k)
model.fit(trainXS,trainY)

preds = model.predict(testXS)

print(f'MSE: ${np.mean(preds != testY)}')
confusion_matrix(testY,preds)

mErr = []
for kn in range(1,k*2):
    knn = KNeighborsClassifier(kn)
    knn.fit(trainXS,trainY)
    pred_i = knn.predict(testXS)
    mErr.append(np.mean(pred_i != testY))

    
plt.xticks(range(1,k*2))
plt.plot(range(1,k*2),mErr,marker='o')
