# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:38:13 2022

@author: mhack
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- Format of read csv

data = pd.read_csv('transaction.csv')

#data = pd.read_csv('transaction.csv', sep=';')

#Summary of the data
data.info()

#Working with Calculations

#Defining Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberofItemsPurchased

#CostPerTransaction Column Calculation
#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#Adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit per Transaction

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup

data['Markup'] = (data['SalesPerTransaction']-data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding Markup

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'],2)

#Combining Data Fields

my_name = 'Michael' + 'Hackleman'

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#my_date = data['Day']+'-'

#Checking columns data type
print(data['Day'].dtype)

#Change Column Type

day = data['Day'].astype(str)
year =data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day +'-' + data['Month'] + '-' + year

data['date'] = my_date

#Using iloc to view specific columns/rows

data.iloc[0] #Views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows

data.iloc[:,2] #all rows 2nd column

data.iloc[4,2] # 4th row 2nd column

#using Split to split the client keywords field
#new_var = column.str.split('separater', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#Creating New columnds for split columns

data["ClientAge"] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2]

#Using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#Using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#Merging files
#Bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv')

#merging files = merge_df = pd.merge(df_old, df_new, on = 'key')

data=pd.merge(data, seasons, on = 'Month')

#How to remove columns using drop function
#df = df.drop('Column Name', axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year','Month'], axis = 1)

#Exporting data into csv

data.to_csv('ValueInc_CleanedSales.csv', index = False)






