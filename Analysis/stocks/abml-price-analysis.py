import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt

abml = yf.download('ABML',start='2021-06-01',end='2022-04-29',progress=False)
abml.head()

plt.plot(abml['Close'])
