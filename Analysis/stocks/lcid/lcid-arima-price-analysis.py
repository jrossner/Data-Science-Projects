import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller

lcid = yf.download('LCID',start='2021-06-01',end='2022-05-03',progress=False)
lcid.head()

plt.plot(lcid['Close'])

timeSeries = lcid['Close']
adfuller(timeSeries)

tsDiff = []
for i in range(1,len(timeSeries)-1):
        tsDiff.append(timeSeries[i+1]-timeSeries[i])
        
tsDiff = pd.Series(tsDiff)
adfuller(tsDiff)

plt.plot(tsDiff)
plot_acf(tsDiff)
plot_pacf(tsDiff)

model = ARIMA(timeSeries, order = (7,1,6))
model_fit = model.fit()
aic = model_fit.aic
model_fit.summary()

models = []
def fit_arima(train,p,d,q):
  model = ARIMA(train, order = (p,d,q))
  model_fit = model.fit()
  aic = model_fit.aic
  models.append({'p': p, 'd': d, 'q': q, 'AIC': aic})

for p in range(0,15):
    for d in range(0,2):
        for q in range(0,7):
            fit_arima(timeSeries,p,d,q)
            print(f'model {p},{d},{q} finished')

#find model with best AIC
df = pd.DataFrame(models)
lowest_AIC_model = df[df["AIC"] == df["AIC"].min()]
best_p,best_d,best_q = int(lowest_AIC_model['p']), int(lowest_AIC_model['d']),int(lowest_AIC_model['q'])

#once best AIC has been found
best_model = ARIMA(timeSeries, order = (best_p, best_d, best_q))
best_fit = best_model.fit()
best_fit.summary()

#check residuals of model
plt.hist(best_fit.resid)
plt.plot(best_fit.resid)
plt.show()

#check fit
fit_vals = best_fit.fittedvalues
plt.plot(timeSeries,color='blue')
plt.plot(fit_vals,color='orange')
plt.show()

#check prediction
length = len(timeSeries)
tl = round(length*.8)
train = timeSeries[:tl]
test = timeSeries[tl:]

model = ARIMA(train, order = (best_p, best_d, best_q))
fit = model.fit()
preds = fit.forecast(steps=2*len(test))

trainD = [x for x in train]

testD = []
for x in train:
    testD.append(None)

for y in test:
    testD.append(y)

predD = []
for y in train:
    predD.append(None)

for y in preds:
    predD.append(y)

plt.plot(trainD,color='blue')
plt.plot(testD,color='orange')
plt.plot(predD,color='red',linestyle='-')
plt.show()
