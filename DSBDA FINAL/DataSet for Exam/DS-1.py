# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:33:27 2023
Perform the following operations using Python on the given datasets
a. Create data subsets
b. Merge Data
c. Sort Data
d. Transposing Data
e. Shape and reshape Data
@author: Puneet P
"""

import os 
import pandas as pd 
import numpy as np
os.chdir("C:\\Users\\HP\\Desktop\\DSBDA TE IT")
cars_data=pd.read_csv('Toyota.csv',index_col=0)
cars_data1=cars_data.copy(deep=True)

## Attribute of the pandas dataframe

cars_data1.ndim
cars_data1.shape
cars_data1.size
cars_data1.index
cars_data1.columns
cars_data1.columns.values
cars_data1.dtypes

## basic methods of the pandas dataframe
cars_data1.memory_usage()
cars_data1.head()
cars_data1.tail()
cars_data1.head(10)
cars_data1.tail(15)
cars_data1.info() # check format of each column
cars_data1.describe() # provide Consize summary of numeric variables
cars_data1['Price'].describe() #Summary of single Column
cars_data1['FuelType'].describe()

## Indexing and selectin data
# label based Lookup
cars_data1.at[9,'FuelType']
cars_data1.at[7,'FuelType']
cars_data1.at[8,'KM']
#index based look ups
cars_data1.iat[4,3]

# Accessing columns
cars_data1['FuelType']


#Access group of rows and columns
cars_data1.loc[:9]
cars_data1.loc[3:9]

cars_data1['FuelType'].loc[3:9]
#------------------------------------------------
## Selecting and Subsetting

#Subset by Selecting columns
cars_sub1=cars_data1[['Price','Age','FuelType','Automatic']]

#subset by selecting rows and columns
cars_sub2=cars_data1[['Price','Age','FuelType']].loc[0:10]
cars_sub3=cars_data1[['Price','Age','FuelType']].loc[cars_data1['FuelType']!='Petrol']

#subset having observations constrained on some column 
cars_sub4=cars_data1[['Price','Age','FuelType']].loc[cars_data1['FuelType']!='Petrol']
  
#-- Create subset of cars_data having Price greater than 15000 and Age less yhan 8
cars_sub5=cars_data1[(cars_data1['Price']>15000)&(cars_data1['Age']<8)]
#-- Create subset of cars_data consuming Petrol
cars_sub6=cars_data1[cars_data1['FuelType']=='Petrol'] 
cars_sub7=cars_data1[cars_data1['FuelType']=='Disel'] 

#------------------------------------------------
# Merging observations obsesrvations using pd.concat()
mergeSet=pd.concat([cars_sub6,cars_sub7])

#Adding new column with calculated field
#- Add a column specifying 5% revision in Price
cars_data1['Revised_Price']=cars_data1['Price']*1.05
#------------------------------------------------
### Sort observations in  column values oder
sorted_on_price=cars_data1.sort_values('Price')
cars_data1.sort_values('Price') # assending order
cars_data1.sort_values('Price',ascending=False) # decending order

cars_data1.sort_values('CC') 

#------------------------------------------------
### Transpose
Transddemo=cars_sub2.transpose()


#--------------------------
#shape and reshape like pivot table
cars_sub2.shape

reshaped_sub2=pd.pivot_table(cars_sub2,index=['Age','FuelType'],values='Price')
print(reshaped_sub2)
reshaped_sub2.shape

print(np.unique(cars_data1['Doors']))
print(np.unique(cars_sub2['Age']))
