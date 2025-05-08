# Q10 - Datasets: employee_info.csv and performance.csv

# a. Clean invalid ages, join dates, and department names
# df_info = pd.read_csv("employee_info.csv")
# df_perf = pd.read_csv("performance.csv")

df_info = df_info[(df_info['Age'] > 18) & (df_info['Age'] < 65)]  # Keeps only reasonable ages
df_info['Join_Date'] = pd.to_datetime(df_info['Join_Date'], errors='coerce')  # Parses dates, coerces invalid ones
df_info['Department'] = df_info['Department'].str.strip().str.title()  # Cleans department names

# b. Combine datasets using EmployeeID
df_combined = pd.merge(df_info, df_perf, on='EmployeeID', how='inner')  # Merges demographic and performance data

# c. Create performance average scores
df_combined['Performance_Avg'] = df_combined[['Score1', 'Score2', 'Score3']].mean(axis=1)  # Average performance score

# d. Bucket performance into categories (Low/Medium/High)
df_combined['Performance_Level'] = pd.cut(df_combined['Performance_Avg'],
                                          bins=[0, 60, 80, 100],
                                          labels=['Low', 'Medium', 'High'])  # Categorizes performance

# e. Correct mismatched or blank department entries
df_combined['Department'] = df_combined['Department'].replace('', 'Unknown')  # Replaces blank departments
