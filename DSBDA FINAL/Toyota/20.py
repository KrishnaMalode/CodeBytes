# Q20 - Dataset: Toyota.csv
# a. Remove all missing values
df.dropna(inplace=True)  # Drops rows with missing values

# b. Display datatypes and concise summary of all numeric variables
dtypes = df.dtypes  # Displays data types of each column
summary = df.describe()  # Summary stats of numeric columns

# c. Remove all duplicate records
df.drop_duplicates(inplace=True)  # Removes duplicate records

# d. Apply Z-score Normalization on Price column
from scipy.stats import zscore
df['Price_ZScore'] = zscore(df['Price'])  # Applies Z-score normalization

# e. Shape and reshape using pivot_table
pivot = df.pivot_table(index='FuelType', values='Price', aggfunc='mean')  # Mean price per fuel type
