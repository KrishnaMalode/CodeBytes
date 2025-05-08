# Q22 - Dataset: Toyota.csv
# a. Display shape and summary and count of missing values in the dataset
shape = df.shape  # Number of rows and columns
summary = df.describe()  # Summary statistics
missing_counts = df.isnull().sum()  # Count of missing values in each column

# b. Remove duplicate records
df.drop_duplicates(inplace=True)  # Removes duplicates

# c. Clean the dataset - Replace missing values with appropriate values
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric columns with mean
df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical columns with mode

# d. Convert datatype of MetColor and Automatic columns to object type
df['MetColor'] = df['MetColor'].astype('object')
df['Automatic'] = df['Automatic'].astype('object')  # Ensures these are treated as categorical
