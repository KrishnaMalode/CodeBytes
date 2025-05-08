# Q29 - Dataset: Salaries.csv
# a. Get the rank and salary of all staff that does not belong to discipline A
non_discipline_a = df[df['discipline'] != 'A'][['rank', 'salary']]  # Excludes discipline A, keeps rank and salary

# b. Get rank, salary, and years of service of all male staff and only female professors
male_staff = df[df['sex'] == 'Male'][['rank', 'salary', 'yrs.service']]  # All male staff
female_professors = df[(df['sex'] == 'Female') & (df['rank'] == 'Prof')][['rank', 'salary', 'yrs.service']]  # Female professors only

# Combine both using concat
combined_subset = pd.concat([male_staff, female_professors])  # Combines the two subsets vertically

# c. Get all Female staff who are either professor or earning more than 75000
female_filter = df[(df['sex'] == 'Female') & ((df['rank'] == 'Prof') | (df['salary'] > 75000))]  # Female professors or salary > 75k

# d. Get the rank and salary of all staff other than professors and who are serving from at least 10 years
long_service_nonprof = df[(df['rank'] != 'Prof') & (df['yrs.service'] >= 10)][['rank', 'salary']]  # Non-professors with ≥10 years service
