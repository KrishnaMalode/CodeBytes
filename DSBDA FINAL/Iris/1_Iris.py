# a. Subset rows where petal length > 1.5 and species is "setosa"
# df = pd.read_csv("Iris.csv")
df_subset = df[(df['petal_length'] > 1.5) & (df['species'] == 'setosa')]  # Filters rows with setosa species and petal length > 1.5

# b. Merge the Iris dataset with a custom species info table (e.g., color or habitat)
# df_info = pd.read_csv("species_info.csv")
df_merged = pd.merge(df, df_info, on='species')  # Merges additional info (e.g., habitat) with main iris dataset

# c. Sort flowers by sepal_width and then by sepal_length
df_sorted = df.sort_values(by=['sepal_width', 'sepal_length'])  # Sorts first by sepal_width, then sepal_length

# d. Transpose the dataset’s first 5 rows to view feature-wise comparisons
transposed = df.head().T  # First 5 rows transposed for feature-wise comparison

# e. Reshape the dataset using melt() and pivot() to transform features into long and wide formats
df_melted = pd.melt(df, id_vars=['species'])  # Converts wide format to long format using 'species' as identifier
df_pivot = df_melted.pivot(index=None, columns='variable', values='value')  # Converts back to wide format
