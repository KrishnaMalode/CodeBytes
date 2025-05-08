# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:21:17 2023
Assignment -3
Visualize the data using Python libraries matplotlib, seaborn by plotting the graphs 

@author: Puneet P
"""


import os 
import pandas as pd 
import numpy as np
# matplotlib library to do visualization
import matplotlib.pyplot as plt

import seabrn as sns
#os.chdir("C:\\Users\\HP\\Desktop\\DSBDA TE IT")


# treat nan missing values as nan
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
cars_data1=cars_data.copy(deep=True)
# Observe shape and values of dataset
cars_data.shape
cars_data.info()
cars_data.isnull().sum()

# removing nan valuse
cars_data.dropna(axis=0,inplace=True)
cars_data.size
cars_data.shape

## ---- Dada Visualization using matplotlib Library -------------------

## SCATTER PLOT
# cars_data.plot()

plt.scatter(cars_data['Age'],cars_data['Price'],c='blue',marker="x")
plt.title("Scatter Plot Car Price vs Age")
plt.xlabel('Agee in months')
plt.ylabel('Price in Dollars')


##  HISTOGRAM
plt.hist(cars_data["KM"])

cars_data.hist('KM')

cars_data["KM"].hist()


# histogram with default arguments
plt.hist(cars_data['KM'],color='blue', edgecolor='white',bins=5)
plt.hist(cars_data['KM'],color='blue', edgecolor='white',bins=8)
 # bins specify the count of distribution range
plt.title("Histogram of Kilometer run")
plt.xlabel('Kelometers')
plt.ylabel('Frequency')
plt.show()
'''
plt. show() starts an event loop, looks for all currently active figure objects, 
and opens one or more interactive windows that display your figure or figures.
'''
## BAR PLOT

# Seting attribute counts, fuelTypes and index based on Dataset
cars_data['FuelType'].value_counts() # get count of categorical variable 
counts=cars_data['FuelType'].value_counts()
fuelTypes=('Petrol', 'Disel','CNG')
index=np.arange(len(fuelTypes))
#counts=[50,100,75]

plt.bar(index,counts,color=['red','green','cyan'])

plt.title("Bar Plot of Fuel Type")
plt.xlabel('Fuel Used')
plt.ylabel('Frequency')

# Bar label
#plt.xticks(index,fuelTypes)
plt.xticks(index,fuelTypes,rotation=90)
plt.show()


## ---------------------------------------------------------------------------
## ---- Dada Visualization using seaborn  library -------------------

# SCATTER PLOT using seaborn regplot() and lmplot() method
sns.set(style='darkgrid')
sns.regplot(x=cars_data['Age'],y=cars_data['Price'])
sns.regplot(fit_reg=False,x=cars_data['Age'],y=cars_data['Price'],marker='+')

##
sns.lmplot(x='Age',y='Price', data=cars_data)
sns.lmplot(x='Age',y='Price', data=cars_data,hue='FuelType')
#Using hue parameter, including another variable to show the fuel types categories 
sns.lmplot(x='Age',y='Price', data=cars_data,hue='FuelType',palette='Set1',size=8)
# set size to make it better visible

##-------HISTOGRAM using seaborn distplot() ----------------
# Histogram with default kernel density estimate
sns.distplot(cars_data['Age'])
# xxx sns.distplot(cars_data['FuelType'])
sns.distplot(cars_data['KM'],bins=10)

# Histogram without kernel density estimate
sns.distplot(cars_data['Age'],kde=False)

## --------BAR PLOT using seaborn countplot()

sns.countplot(x='FuelType',data=cars_data)

#We can have grouped bar plot by setting hue as another categorical vriable
# Grouped bar plot of FuelType and Automatic
sns.countplot(x='FuelType',data=cars_data,hue='Automatic')

##--------- BOX PLOT  using seaborn boxplot()-----
sns.boxplot(y=cars_data['Price'])
# box plot for numerical data vs categorical data
sns.boxplot(y=cars_data['Price'], x=cars_data['FuelType'])
