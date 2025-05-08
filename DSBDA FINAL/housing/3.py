# a. Subset houses with median income > 5 and average rooms < 6
# df = pd.read_csv("housing.csv")
df_subset = df[(df['median_income'] > 5) & ((df['total_rooms'] / df['households']) < 6)]

# b. Merge with regional lookup (latitude/longitude to regions)
# df_regions = pd.read_csv("regions.csv")
df_merged = pd.merge(df, df_regions, on=['latitude', 'longitude'])

# c. Sort by median_house_value and population
df_sorted = df.sort_values(by=['median_house_value', 'population'])

# d. Transpose statistical summary for all features
summary = df.describe().T

# e. Reshape to view average house value across income and housing age bins
df['income_bin'] = pd.cut(df['median_income'], bins=3)
df['age_bin'] = pd.cut(df['housing_median_age'], bins=3)
pivot_table = df.pivot_table(index='income_bin', columns='age_bin', values='median_house_value', aggfunc='mean')
