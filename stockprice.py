# Machine Learning project
#importing libraries
import datetime as dt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

style.use("ggplot")
dataframe = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

#dataframe['100ma'] = dataframe['Adj Close'].rolling(window=100, min_periods = 0).mean()
dataframe.dropna(inplace=True)

#ohlc- open high low close
df_ohlc = dataframe['Adj Close'].resample('10D').ohlc()
df_volume = dataframe['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)
# converting df dates to m dates w matplotlib

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())


ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan = 1, colspan = 1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup ='g')

ax2.fill_between(df_volume.index.map(mdates.date2num, df_volume.values, 0))


plt.show()