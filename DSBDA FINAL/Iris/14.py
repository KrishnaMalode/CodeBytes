# Q14 - Dataset: Iris.csv
# a. Check for and handle any duplicated rows or missing values (insert some intentionally for practice)
# df = pd.read_csv("Iris.csv")
df.drop_duplicates(inplace=True)  # Removing duplicate rows
df.fillna(df.mean(numeric_only=True), inplace=True)  # Filling missing numeric values with column mean

# b. Combine with an external species characteristics table (e.g., color, blooming time)
# df_species = pd.read_csv("species_info.csv")
# Example: Assuming df_species contains 'species', 'color', 'blooming_time'
df_combined = pd.merge(df, df_species, on='species')  # Merging on species column

# c. Normalize petal/sepal measurements
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']] = scaler.fit_transform(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

# d. Add a size_ratio = petal_length / sepal_length column
df['size_ratio'] = df['petal_length'] / df['sepal_length']  # Creating new derived feature
