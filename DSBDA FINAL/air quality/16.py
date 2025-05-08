# a. Read data set and display summary
# df = pd.read_csv("airquality.csv")
summary = df.describe(include='all')  # Summary statistics for all columns

# b. Create data subsets:
subset1 = df.iloc[11:50]  # Observations in range 11 to 49 (inclusive of 11th index, up to 49th)
subset2 = df[df['Temp'] < 60]  # Subset with Temp values less than 60

# c. Merge observations of any two subsets
df_merged = pd.concat([subset1, subset2], axis=0)  # Merge the two subsets vertically

# d. Apply Sort Data on Temp values
df_sorted = df.sort_values(by='Temp')  # Sort the full dataset based on Temp values
