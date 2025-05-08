# a. Subset wines with quality ≥ 7 and alcohol > 10%
# df = pd.read_csv("WineQT.csv")
df_subset = df[(df['quality'] >= 7) & (df['alcohol'] > 10)]

# b. Merge red and white wines with a new 'type' column
# df_red = pd.read_csv("red.csv"); df_red['type'] = 'red'
# df_white = pd.read_csv("white.csv"); df_white['type'] = 'white'
df_combined = pd.concat([df_red, df_white], axis=0)  # Combined dataset with wine type

# c. Sort wines by citric acid and residual sugar
df_sorted = df.sort_values(by=['citric acid', 'residual sugar'])

# d. Transpose summary statistics of chemical properties grouped by quality
summary = df.groupby('quality').mean().T

# e. Pivot table for average values of key features by wine quality
pivot_table = df.pivot_table(index='quality', values=['alcohol', 'residual sugar', 'citric acid'], aggfunc='mean')
