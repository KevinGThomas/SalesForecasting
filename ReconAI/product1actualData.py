# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:40:48 2018

@author: keV
"""

#%%
from datetime import datetime
import warnings
#import time
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from pylab import rcParams
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df1=pd.read_csv('ActualData.csv')
df = df1.loc[df1['UPC'] == 1234512345]
#df = df1.loc[df1['UPC'] == 1234567890]
# Determine the date
df['date'] = pd.to_datetime(df.assign(day=1, month=1)[['Year', 'month', 'day']])+pd.to_timedelta(df.Week*7, unit='days')
df.head()
#%%

df[' Sales '] = df[' Sales '].str.replace(',', '')
df[' Sales '] = df[' Sales '].astype(float)
df.head()
#%%
newdf = pd.DataFrame(df,columns=['date'])
def sum_scores(d):
    return df[(df['date']==d)][[' Sales ']].sum()

newdf[['Total Sales']] = newdf['date'].transform(sum_scores)
newdf.drop_duplicates(subset ="date", 
                     keep = "first", inplace = True) 
newdf.head()
#newdf.index=pd.DateTimeIndex(frq="w",start=0,periods=500)
#%%
#dates = [datetime.strptime(date, '%Y/%m/%d').date() for date in newdf['date']]
#plt.plot(newdf['date'],newdf['Total Sales'])
#plt.show()
ax=plt.gca()
rcParams['figure.figsize'] = 10, 4
xfmt = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
plt.xticks( rotation=25 )
#plt.xticks( rotation=25 )
ax=plt.gca()
ax.xaxis_date()
#axes.set_ylim([ymin,ymax])
#ax=plt.ylim((11500000,12300000))
#ax.ticklabel_format(useOffset=False, style='plain')
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
plt.plot(newdf['date'],newdf['Total Sales'])
plt.show()
#%%