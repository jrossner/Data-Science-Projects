import pandas as pd

with open('./Raw-Data-Files/iris/iris.data') as raw:
    data = raw.read().splitlines()

data[0:5]

sData = [obs.split(',') for obs in data]

sData[0:5]

df = pd.DataFrame(sData, columns=('sepal-length','sepal-width','petal-length','petal-width','iris'))
df.dtypes

numCols = ['sepal-length','sepal-width','petal-length','petal-width']
for col in numCols:
    df[col] = df[col].astype(float)

df.head()
