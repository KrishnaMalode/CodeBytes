# a. Create data subsets
# df = pd.read_csv("Toyota.csv")
df_price_subset = df[df['Price'] > 15000]  # Subset of cars priced above 15000
df_age_subset = df[df['Age'] < 5]  # Subset of cars younger than 5 years

# b. Merge data
df_merged = pd.merge(df_price_subset, df_age_subset, on='Car_ID')  # Merge on Car_ID

# c. Sort by Price column
df_sorted = df.sort_values(by='Price')

# d. Transpose the first 5 rows
transposed = df.head().T

# e. Shape and reshape using melt and pivot
df_melted = pd.melt(df, id_vars=['FuelType'])  # Melts the dataset based on FuelType
df_pivot = df_melted.pivot(index=None, columns='variable', values='value')  # Converts long to wide
