import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

lcid = yf.download('LCID',start='2021-06-01',end='2022-05-03',progress=False)
lcid.head()

price = [x for x in lcid['Close'][5:]]

prev1,prev2,prev3,prev4,prev5 = [],[],[],[],[]
for i in range(5,len(lcid['Close'])):
    prev1.append(lcid['Close'][i-1])
    prev2.append(lcid['Close'][i-2])
    prev3.append(lcid['Close'][i-3])
    prev4.append(lcid['Close'][i-4])
    prev5.append(lcid['Close'][i-5])

df = pd.DataFrame(list(zip(price,prev1,prev2,prev3,prev4,prev5)),columns=['Price','Prev1','Prev2','Prev3','Prev4','Prev5'])
df.head()

df['Res'] = [1 if x > y else 0 for x,y in zip(df['Price'],df['Prev1'])]
df['P1'] = [1 if x > y else 0 for x,y in zip(df['Prev1'],df['Prev2'])]
df['P2'] = [1 if x > y else 0 for x,y in zip(df['Prev2'],df['Prev3'])]
df['P3'] = [1 if x > y else 0 for x,y in zip(df['Prev3'],df['Prev4'])]
df['P4'] = [1 if x > y else 0 for x,y in zip(df['Prev4'],df['Prev5'])]
df.head()

tl = round(len(df)*.9)
trainX = df[:tl][['P1','P2','P3','P4']]
trainY = df[:tl]['Res']
testX = df[tl:][['P1','P2','P3','P4']]
testY = df[tl:]['Res']

model = LogisticRegression()
model.fit(trainX,trainY)

pred = model.predict(testX)
mat = metrics.confusion_matrix(testY,pred)

model.coef_
model.intercept_
model.classes_
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                print(f'For input {a},{b},{c},{d}, predicted probability: {model.predict_proba([[a,b,c,d]])}')

predProb = model.predict_proba(testX)[::,1]
fpr,tpr,_ = metrics.roc_curve(testY,predProb)
auc = metrics.roc_auc_score(testY,predProb)
plt.plot(fpr,tpr)

predsT = model.predict(trainX)
matT = metrics.confusion_matrix(trainY,predsT)
matT
cm = metrics.ConfusionMatrixDisplay(matT,['down','up'])
cm.plot()

#accuracy
(96+24)/(96+16+69+24)
#fp
16/(16+24)
#fn
69/(96+69)
#tp
24/(24+69)
#tn
96/(96+69)

#Predicting whole data set
X = df[:][['P1','P2','P3','P4']]
Y = df[:]['Res']

preds = model.predict(X)
mat = metrics.confusion_matrix(Y,preds)
mat
cm = metrics.ConfusionMatrixDisplay(mat,['down','up'])
cm.plot()

#accuracy
(107+25)/(107+20+76+25)
#fp
20/(20+25)
#fn
76/(76+107)
#tp
25/(20+25)
#tn
107/(107+76)

pp = model.predict_proba(X)[::,1]
fpr,tpr,_ = metrics.roc_curve(Y,pp)
auc = metrics.roc_auc_score(Y,pp)
plt.plot(fpr,tpr)

#training on entire data set
modelf = LogisticRegression()
modelf.fit(X,Y)

pred = modelf.predict(X)
mat = metrics.confusion_matrix(Y,pred)

cm = metrics.ConfusionMatrixDisplay(mat,['down','up'])
cm.plot()

pp = modelf.predict_proba(X)[::,1]
fpr,tpr,_ = metrics.roc_curve(Y,pp)
auc = metrics.roc_auc_score(Y,pp)
plt.plot(fpr,tpr)
(112+15)
84+17
