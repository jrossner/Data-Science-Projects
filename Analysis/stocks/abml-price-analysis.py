import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

abml = yf.download('ABML',start='2021-06-01',end='2022-04-29',progress=False)
abml.head()

plt.plot(abml['Close'])

timeSeries = abml['Close']
tsDiff = []
for i in range(1,len(timeSeries)-1):
        tsDiff.append(timeSeries[i+1]-timeSeries[i])
        
tsDiff = pd.Series(tsDiff)

plt.plot(tsDiff)
plot_acf(tsDiff)
plot_pacf(tsDiff)


model = ARIMA(timeSeries, order = (2,1,2))
model_fit = model.fit()
aic = model_fit.aic
model_fit.summary()

models = []
def fit_arima(train,p,d,q):
  model = ARIMA(train, order = (p,d,q))
  model_fit = model.fit()
  aic = model_fit.aic
  models.append({'p': p, 'd': d, 'q': q, 'AIC': aic})

for p in range(0,10):
    for d in range(0,3):
        for q in range(0,10):
            fit_arima(timeSeries,p,d,q)
            print(f'model {p},{d},{q} finished')
  
#find model with best AIC
df = pd.DataFrame(models)
lowest_AIC_model = df[df["AIC"] == df["AIC"].max()]
best_p,best_d,best_q = int(lowest_AIC_model['p']), int(lowest_AIC_model['d']),int(lowest_AIC_model['q'])

#once best AIC has been found
best_model = ARIMA(timeSeries, order = (best_p, best_d, best_q))
best_fit = best_model.fit()
best_fit.summary()
