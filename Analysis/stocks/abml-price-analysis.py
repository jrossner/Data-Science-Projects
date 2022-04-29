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
    try:
        tsDiff.append(timeSeries[i+1]-timeSeries[i])

plt.plot(tsDiff)
