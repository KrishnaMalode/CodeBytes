
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# ---------------------------
# Using Iris Dataset
# ---------------------------

# Load Iris dataset
iris_data = load_iris(as_frame=True)
iris_df = iris_data.frame

# a. Subset data - flowers with petal length > 1.5 and species 'setosa'
subset_iris = iris_df[(iris_df['petal length (cm)'] > 1.5) & (iris_df['target'] == 0)]
print("Subset of Iris data:")
print(subset_iris.head(), '\n')

# b. Merge - adding species name from target column
iris_df = iris_df.merge(pd.DataFrame(iris_data.target_names, columns=["species"]).reset_index(),
                        left_on='target', right_on='index', how='left')
print("Merged Iris data with species names:")
print(iris_df[['sepal length (cm)', 'species']].head(), '\n')

# c. Sort data - by sepal width and sepal length
sorted_iris = iris_df.sort_values(by=['sepal width (cm)', 'sepal length (cm)'], ascending=[False, True])
print("Sorted Iris data:")
print(sorted_iris.head(), '\n')

# d. Transpose - transpose the first 5 rows
print("Transposed Iris data:")
print(iris_df.head().T, '\n')

# e. Reshape using melt and pivot
melted_iris = pd.melt(iris_df, id_vars=['species'], value_vars=iris_df.columns[:4])
pivot_iris = melted_iris.pivot_table(index='variable', columns='species', values='value', aggfunc='mean')
print("Reshaped Iris data:")
print(pivot_iris, '\n')

# ---------------------------
# Using Wine Quality Dataset
# ---------------------------

# Load wine dataset
wine_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

# a. Subset - quality >= 7 and alcohol > 10
subset_wine = wine_df[(wine_df['quality'] >= 7) & (wine_df['alcohol'] > 10)]
print("Subset of Wine data:")
print(subset_wine.head(), '\n')

# b. Merge - Simulate merge with wine type
white_wine_df = wine_df.copy()
white_wine_df['type'] = 'white'
red_wine_df = wine_df.copy()
red_wine_df['type'] = 'red'
merged_wine = pd.concat([red_wine_df, white_wine_df])
print("Merged Wine data with type column:")
print(merged_wine[['alcohol', 'quality', 'type']].head(), '\n')

# c. Sort - by citric acid and residual sugar
sorted_wine = merged_wine.sort_values(by=['citric acid', 'residual sugar'], ascending=[False, True])
print("Sorted Wine data:")
print(sorted_wine.head(), '\n')

# d. Transpose summary stats
print("Transposed summary statistics:")
print(merged_wine.describe().T, '\n')

# e. Reshape - pivot table of average alcohol by quality and type
pivot_wine = merged_wine.pivot_table(index='quality', columns='type', values='alcohol', aggfunc='mean')
print("Reshaped Wine data (Pivot Table):")
print(pivot_wine)
