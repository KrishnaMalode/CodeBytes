# Q28 - Dataset: Salaries.csv
# a. Create data subsets
# df = pd.read_csv("Salaries.csv")
subset1 = df[df['discipline'] == 'A']  # Subset of faculty from discipline A
subset2 = df[df['sex'] == 'Female']  # Subset of female staff

# b. Merge Data
merged_df = pd.merge(subset1, subset2, how='inner', on=['rank', 'discipline', 'sex'])  # Merge on common columns

# c. Sort Data
df_sorted = df.sort_values(by='salary', ascending=False)  # Sorts by salary in descending order

# d. Transposing Data
transposed = df.head(5).T  # Transpose the first 5 rows for feature-wise comparison

# e. Shape and reshape Data
df_melted = pd.melt(df, id_vars=['rank', 'sex'], value_vars=['salary', 'yrs.service', 'yrs.since.phd'])  # Convert to long format

df_pivot = df.pivot_table(index='rank', columns='sex', values='salary', aggfunc='mean')  # Pivot to get avg salary by rank and sex
