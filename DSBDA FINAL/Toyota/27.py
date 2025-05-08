# Q27 - Dataset: Toyota.csv
# a. Remove missing values
df.dropna(inplace=True)  # Drops rows with any missing values

# b. Display datatypes and concise summary of all numeric variables
dtypes = df.dtypes  # Shows data types of all columns
summary = df.describe()  # Summary stats for numeric features

# c. Remove all duplicate records 
df.drop_duplicates(inplace=True)  # Removes duplicated rows

# d. Apply Z-Score Normalization on Price Column
from scipy.stats import zscore
df['Price_ZScore'] = zscore(df['Price'])  # Z-score normalization on price

# e. Shape and reshape using pivot_table
pivot = df.pivot_table(index='FuelType', values='Price', aggfunc='mean')  # Shows average price per fuel type
