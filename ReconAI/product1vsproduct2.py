# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:18:16 2018

@author: keV
"""
import pandas as pd
from pylab import rcParams
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
#%%
df_read=pd.read_csv('ActualData.csv')
#newdf=pd.read_csv('ActualData.csv')
def sales_product(df):
    df['date'] = pd.to_datetime(df.assign(day=1, month=1)[['Year', 'month', 'day']])+pd.to_timedelta(df.Week*7, unit='days')
    df.head()
    df[' Sales '] = df[' Sales '].str.replace(',', '')
    df[' Sales '] = df[' Sales '].astype(float)
    df.head()
def remove_columns(df):
    newdf = pd.DataFrame(df,columns=['date'])
    def sum_scores(d):
        return df[(df['date']==d)][[' Sales ']].sum()
    newdf[['Total Sales']] = newdf['date'].transform(sum_scores)
    newdf.drop_duplicates(subset ="date", 
                     keep = "first", inplace = True) 
    print(newdf.head())
    return newdf
df1 = df_read.loc[df_read['UPC'] == 1234567890]
df2 = df_read.loc[df_read['UPC'] == 1234512345]
sales_product(df1)
sales_product(df2)
newdf1=remove_columns(df1)
newdf2=remove_columns(df2)
print(df1.head(5))
print(df2.head())

#%%
ax=plt.gca()
rcParams['figure.figsize'] = 10, 4
xfmt = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
plt.xticks( rotation=25 )
ax=plt.gca()
ax.xaxis_date()
#axes.set_ylim([ymin,ymax])
#ax=plt.ylim((11500000,12300000))
#ax.ticklabel_format(useOffset=False, style='plain')
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
plt.plot(newdf1['date'],newdf1['Total Sales'],label='Product 1')
plt.plot(newdf2['date'],newdf2['Total Sales'],label='Product 2')
plt.plot()
ax.legend()
plt.show()
#%%