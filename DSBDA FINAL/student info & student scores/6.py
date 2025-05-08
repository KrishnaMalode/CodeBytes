# Q6 - Datasets: student_info.csv and student_scores.csv

# a. Clean both datasets to handle missing values, incorrect formats, and inconsistent entries
df_info = pd.read_csv("student_info.csv")
df_scores = pd.read_csv("student_scores.csv")
df_info = df_info.drop_duplicates()  # Removes duplicate student info records
df_scores = df_scores.drop_duplicates()  # Removes duplicate score records
df_info = df_info.fillna({'Age': df_info['Age'].median(), 'Email': 'unknown@example.com'})  # Imputes missing values
df_scores = df_scores.fillna(0)  # Fills missing scores with 0 as default

# b. Remove invalid scores (e.g., -1 in Science)
df_scores = df_scores[df_scores['Science'] >= 0]  # Keeps only valid Science scores (non-negative)

# c. Convert Grade to string format like "Grade 10"
df_info['Grade'] = df_info['Grade'].astype(str).apply(lambda x: "Grade " + x)  # Converts Grade to formatted string

# d. Perform an inner join and analyze which students are present in both datasets
df_merged = pd.merge(df_info, df_scores, on='StudentID', how='inner')  # Joins datasets on StudentID (inner join)

# e. Handle any mismatches (e.g., StudentID = 106 is not in student_info.csv)
missing_students = set(df_scores['StudentID']) - set(df_info['StudentID'])  # Finds mismatched IDs
df_mismatches = df_scores[df_scores['StudentID'].isin(missing_students)]  # Gets score records not found in info table
