# Q23 - Dataset: Toyota.csv
# a. Remove duplicate records from dataset and display concise summary
df.drop_duplicates(inplace=True)  # Removing duplicates
summary = df.describe()  # Concise summary of numeric data

# b. Create subset selecting columns 'Price', 'Age', 'FuelType' and initial 10 records
subset = df[['Price', 'Age', 'FuelType']].head(10)  # Subset with first 10 rows and selected columns

# c. Transpose of this subset
transposed = subset.T  # Transposing rows to columns

# d. Apply mean-max normalization on HP column
df['HP_mean_max_norm'] = (df['HP'] - df['HP'].mean()) / (df['HP'].max() - df['HP'].min())  # Mean-max normalization
