import pandas as pd
import matplotlib.pyplot as plt

with open('/Raw-Data-Files/iris/iris.data') as raw:
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
