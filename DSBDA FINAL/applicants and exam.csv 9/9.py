# Q9 - Datasets: applicants.csv and exam_scores.csv

# a. Clean up inconsistent formatting in names and missing test scores
# df_applicants = pd.read_csv("applicants.csv")
# df_scores = pd.read_csv("exam_scores.csv")

df_applicants['Name'] = df_applicants['Name'].str.strip().str.title()  # Standardize name formatting
df_scores = df_scores.dropna(subset=['Test_Score'])  # Remove records with missing test scores

# b. Join on ApplicationID to combine personal data with scores
df_combined = pd.merge(df_applicants, df_scores, on='ApplicationID', how='inner')  # Merges both datasets on ApplicationID

# c. Normalize test scores
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_combined['Normalized_Score'] = scaler.fit_transform(df_combined[['Test_Score']])  # Scales test scores between 0 and 1

# d. Convert Admission_Status to binary labels (1 = admitted)
df_combined['Admission_Status_Binary'] = df_combined['Admission_Status'].map({'Admitted': 1, 'Rejected': 0})  # Converts categorical status to numeric

# e. Remove duplicate applications and fix invalid test score entries
df_combined = df_combined.drop_duplicates(subset='ApplicationID')  # Removes duplicate applications
df_combined = df_combined[df_combined['Test_Score'] >= 0]  # Removes any entries with invalid test scores (e.g., negative)
