# Q12 - Dataset: StudentsPerformance.csv

# a. Check for and impute any missing test scores (math, reading, writing)
# df = pd.read_csv("StudentsPerformance.csv")
df[['math score', 'reading score', 'writing score']] = df[['math score', 'reading score', 'writing score']].fillna(df.mean())  # Fills missing scores with column means

# b. Create an overall AverageScore column
df['AverageScore'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)  # Calculates mean score per student

# c. Bucket students into performance bands (e.g., Excellent, Average, Poor)
df['PerformanceBand'] = pd.cut(df['AverageScore'],
                               bins=[0, 60, 80, 100],
                               labels=['Poor', 'Average', 'Excellent'])  # Categorizes performance

# d. Check for inconsistent or duplicate student records
df = df.drop_duplicates()  # Removes duplicate records

# e. Encode gender, lunch, and test preparation course using Label Encoding
df['gender_encoded'] = le.fit_transform(df['gender'])  # Encodes gender
df['lunch_encoded'] = le.fit_transform(df['lunch'])  # Encodes lunch
df['test_prep_encoded'] = le.fit_transform(df['test preparation course'])  # Encodes test preparation
