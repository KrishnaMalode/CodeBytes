# Q26 - Dataset: Toyota.csv
# a. Sort observations on Price values order
df_sorted = df.sort_values(by='Price')  # Sorts in ascending price order

# b. Create subset by selecting columns, selecting rows and columns
subset_cols = df[['Price', 'FuelType', 'Age']]  # Select specific columns
subset_rows_cols = df.loc[0:9, ['Price', 'Age']]  # First 10 rows with selected columns

# c. Create subset of cars data having Price > 15000 and Age < 8
df_filtered = df[(df['Price'] > 15000) & (df['Age'] < 8)]  # Condition based filtering

# d. Create subset of cars data consuming Petrol
df_petrol = df[df['FuelType'] == 'Petrol']  # Filters petrol cars only

# e. Apply decimal normalization on Price column 
df['Price_DecimalNorm'] = df['Price'] / (10 ** len(str(int(df['Price'].max()))))  # Decimal normalization
