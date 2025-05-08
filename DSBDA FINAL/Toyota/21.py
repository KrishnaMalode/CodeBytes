# Q21 - Dataset: Toyota.csv
# a. Get unique values of categorical ‘Doors’
unique_doors = df['Doors'].unique()  # Lists unique values in 'Doors' column

# b. Transform all values in same format
df['Doors'] = df['Doors'].astype(str).str.strip().str.lower().replace({'three': '3', 'four': '4'})  # Consistent format

# c. Apply Decimal scaling normalization on HP column
df['HP_DecimalNorm'] = df['HP'] / (10 ** len(str(df['HP'].abs().max()).split('.')[0]))  # Decimal scaling normalization
