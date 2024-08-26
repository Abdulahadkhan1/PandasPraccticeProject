from enum import unique
import pandas as pd
import numpy as np
from pydantic.v1.utils import unique_list

df1 = pd.read_csv('covid_19_india.csv')
df2 = pd.read_csv('StatewiseTestingDetails.csv')

df1.rename(columns={"State/UnionTerritory":"State"}, inplace=True)


duplicate_list = pd.merge(df1, df2)
unique_list = duplicate_list['State'].unique().tolist()
len(unique_list)


df2 = df2.fillna(0)

data1 = df1[df1['State'].isin(unique_list) & (df1['Date'] >= '2020-04-17') & (df1['Date'] <= '2021-08-10')]
print(data1)
data2 = df2[df2['State'].isin(duplicate_list)]
print(data2)
data1 = data1.groupby('State')[['Sno', 'Cured', 'Deaths', 'Confirmed']].sum()
data2 = data2.groupby('State')[['TotalSamples', 'Positive']].sum()
data2['Positive Rate'] = data2['Positive'] / data2['TotalSamples']
print(data2)



pd.merge(data1, data2, on='State')

data1= pd.DataFrame()
data2 = pd.DataFrame()
print(data2)