# a. Subset students with math score > 80 and who completed the test preparation course
# df = pd.read_csv("StudentsPerformance.csv")
df_subset = df[(df['math score'] > 80) & (df['test preparation course'] == 'completed')]

# b. Merge with demographic table (subset for socioeconomic status)
# df_demo = pd.read_csv("demographic.csv")
df_merged = pd.merge(df, df_demo, on='student_id')  # Merges datasets using student_id

# c. Sort by reading score and writing score in descending order
df_sorted = df.sort_values(by=['reading score', 'writing score'], ascending=[False, False])

# d. Transpose average scores by gender across all subjects
avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().T

# e. Pivot table for average scores across lunch and test prep status
pivot_table = df.pivot_table(index='lunch', columns='test preparation course',
                              values=['math score', 'reading score', 'writing score'], aggfunc='mean')
