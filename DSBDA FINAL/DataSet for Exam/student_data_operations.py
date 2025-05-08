
import pandas as pd

# Load datasets
students = pd.read_csv("students.csv")
activities = pd.read_csv("activities.csv")

# a. Create Data Subsets
subset_math = students[['Name', 'Math']]
subset_grade_11 = students[students['Grade'] == 11]
subset_high_science = students[students['Science'] > 85]

# b. Merge Data
merged_df = pd.merge(students, activities, on='StudentID')

# c. Sort Data
sorted_math = students.sort_values(by='Math', ascending=False)
sorted_grade_science = students.sort_values(by=['Grade', 'Science'], ascending=[True, False])

# d. Transpose Data
alice_scores = students[students['Name'] == 'Alice'].set_index('Name').loc[:, ['Math', 'Science', 'History']].T
transposed_all = students.drop(columns='Name').set_index('StudentID').T

# e. Shape and Reshape Data
shape_original = students.shape
scores_array = students[['Math', 'Science', 'History']].values
reshaped_array = scores_array.reshape(5, 3)  # same shape as original, but shows the concept
long_format = pd.melt(students, id_vars=['StudentID', 'Name'], value_vars=['Math', 'Science', 'History'],
                      var_name='Subject', value_name='Score')

# Print outputs
print("a. Subsets:")
print("Math Subset:\n", subset_math)
print("\nGrade 11 Students:\n", subset_grade_11)
print("\nStudents with Science > 85:\n", subset_high_science)

print("\nb. Merged Data:\n", merged_df)

print("\nc. Sorted Data:")
print("Sorted by Math:\n", sorted_math)
print("\nSorted by Grade then Science:\n", sorted_grade_science)

print("\nd. Transposed Data:")
print("Alice's Transposed Scores:\n", alice_scores)
print("\nTransposed Dataset:\n", transposed_all)

print("\ne. Shape and Reshape:")
print("Original Shape:", shape_original)
print("Reshaped Array:\n", reshaped_array)
print("\nLong Format Data:\n", long_format)
