# Q15 - Dataset: Toyota.csv
# a. Data cleaning
# df = pd.read_csv("Toyota.csv")
df.dropna(inplace=True)  # Removing rows with missing values

# b. Data integration
# Assume merging with another table df_specs on Car_ID
# df_specs = pd.read_csv("specifications.csv")
# df_merged = pd.merge(df, df_specs, on='Car_ID')

# c. Data transformation
df['Price'] = df['Price'] * 1.1  # Example transformation: Adjust price by inflation rate

# d. Error correcting
df['Doors'] = df['Doors'].replace({'three': 3, 'four': 4})  # Correcting inconsistent values in 'Doors'
