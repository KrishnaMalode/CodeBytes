# Q7 - Datasets: student_info.csv and student_scores.csv

# a. Clean both datasets to handle missing values, incorrect formats, and inconsistent entries
# df_info = pd.read_csv("student_info.csv")
# df_scores = pd.read_csv("student_scores.csv")
df_info['Age'] = df_info['Age'].fillna(df_info['Age'].median())  # Fills missing age with median
df_info['Email'] = df_info['Email'].fillna('unknown@example.com')  # Fills missing emails
df_info['History'] = df_info['History'].fillna(0)  # Fills missing history scores

# b. Identify and fill or remove missing values in Age, Email, and History
df_info = df_info.dropna(subset=['Age', 'Email', 'History'])  # Ensures no missing values remain in key columns

# c. Standardize email addresses and correct improperly formatted ones (e.g., "eva.email.com")
df_info['Email'] = df_info['Email'].apply(lambda x: x if '@' in x else x.replace('.', '@', 1))  # Fixes missing '@'

# d. Create a new column for average score across subjects
df_scores['Average'] = df_scores[['Math', 'Science', 'History']].mean(axis=1)  # Adds average column

# e. Add a binary column HighPerformer (1 if avg score > 85, else 0)
df_scores['HighPerformer'] = df_scores['Average'].apply(lambda x: 1 if x > 85 else 0)  # Tags high performers
