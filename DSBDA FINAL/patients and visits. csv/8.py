# Q8 - Datasets: patients.csv and visits.csv

# a. Fill or drop missing diagnosis codes and ages
# df_patients = pd.read_csv("patients.csv")
# df_visits = pd.read_csv("visits.csv")
df_visits['Diagnosis'] = df_visits['Diagnosis'].fillna('Unknown')  # Fills missing diagnosis
df_patients = df_patients[df_patients['Age'] <= 120]  # Drops patients with invalid ages over 120

# b. Standardize gender values (e.g., “M”, “Male”, “F” → “Male”, “Female”)
df_patients['Gender'] = df_patients['Gender'].replace({'M': 'Male', 'F': 'Female'})  # Maps short forms to full
df_patients['Gender'] = df_patients['Gender'].str.title()  # Standardizes casing

# c. Merge patient info with visits
df_merged = pd.merge(df_patients, df_visits, on='PatientID', how='inner')  # Combines data by PatientID

# d. Group data to get total visits and unique diagnoses per patient
visit_summary = df_merged.groupby('PatientID').agg({'VisitID': 'count', 'Diagnosis': pd.Series.nunique})  # Visit count and unique diagnosis count

# e. Correct out-of-range values (e.g., age > 120)
df_patients.loc[df_patients['Age'] > 120, 'Age'] = 120  # Caps age at 120 if still any outliers exist
