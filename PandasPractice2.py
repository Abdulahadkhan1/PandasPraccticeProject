import pandas as pd
import numpy as np
df1 = pd.read_csv('covid_19_india.csv')
df2 = pd.read_csv('StatewiseTestingDetails.csv')

df2 = pd.fillna(0)

data1 = df1[df1['State'].isin(unique_list) & (df1['Date'] >= '2020-04-17') & (df1['Date'] <= '2021-08-10')]
data2 = df2[df2['State'].isin(duplicate_list)]
data1 = data1.groupby('State')[['Sno', 'Cured', 'Deaths', 'Confirmed']].sum()
data2 = data2.groupby('State')[['TotalSamples', 'Positive']].sum()
data2['Positive Rate'] = data2['Positive'] / data2['TotalSamples']
pd.merge(data1, data2, on='State')

data1= pd.DataFrame()
data2 = pd.DataFrame()

print(data1)
print(data2)