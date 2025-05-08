# Q19 - Dataset: Toyota.csv
# a. Sort observations on Price values order
df_sorted = df.sort_values(by='Price')  # Sorts cars by price in ascending order

# b. Create subset by selecting columns, selecting rows and columns
subset_cols = df[['Price', 'Age', 'FuelType']]  # Selecting specific columns
subset_rows_cols = df.loc[0:4, ['Price', 'Age']]  # First 5 rows with selected columns

# c. Create subset of cars data having Price > 15000 and Age < 8
df_subset = df[(df['Price'] > 15000) & (df['Age'] < 8)]  # Filters cars based on price and age condition

# d. Create subset of cars data consuming Petrol
df_petrol = df[df['FuelType'] == 'Petrol']  # Filters rows with FuelType = Petrol

# e. Apply decimal normalization on Price column
df['Price_DecimalNorm'] = df['Price'] / (10 ** len(str(df['Price'].abs().max()).split('.')[0]))  # Decimal scaling
