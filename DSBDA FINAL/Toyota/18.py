# Q18 - Dataset: Toyota.csv
# a. Remove missing values
# df = pd.read_csv("Toyota.csv")
df.dropna(inplace=True)  # Removes all rows with any missing values

# b. Set Doors value to uniform format
df['Doors'] = df['Doors'].astype(str).str.lower().replace({'three': '3', 'four': '4', 'five': '5'})  # Unifying all formats

# c. Provide concise summary of all numeric variables
summary = df.describe()  # Shows count, mean, std, min, max of all numerical columns

# d. Remove all duplicate records
df.drop_duplicates(inplace=True)  # Removes duplicated rows

# e. Get dummies for categorical data FuelType (One hot Encoding)
df = pd.get_dummies(df, columns=['FuelType'], drop_first=True)  # Encodes FuelType with one-hot encoding
