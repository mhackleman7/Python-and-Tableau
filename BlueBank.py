# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:31:54 2022

@author: mhack
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#Method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)

#transform to data frame
loandata = pd.DataFrame(data)

#Finding unique values for the purpose column
loandata['purpose'].unique()

#Describe the data
loandata.describe()

#Describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income
   
#FICO Score

fico = 700

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

fico = 250

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico >= 780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)
    
#Applying for loops to loandata
#using first 10

length =len(loandata)
ficocat = []
for x in range(0,9578):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 780:
        cat = 'Good'
    elif category >=780:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[col name] condition, new column name] = 'value if condition is met'

# for interest rates a new column is wanted, rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'
        
#Number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecatplot = loandata.groupby(['purpose']).size()
purposecatplot.plot.bar(color = 'blue', width = 0.2)
plt.show()

#Scatterplots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)














