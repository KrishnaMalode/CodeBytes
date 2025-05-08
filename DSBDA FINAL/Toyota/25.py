# Q25 - Dataset: Toyota.csv
# a. Create subset selecting columns 'Price', 'Age', 'FuelType', 'Automatic'
subset1 = df[['Price', 'Age', 'FuelType', 'Automatic']]  # Subset of specified columns

# b. Create subset having records of all Petrol vehicles 
petrol_subset = df[df['FuelType'] == 'Petrol']  # Filters only petrol vehicles

# c. Create subset of cars’ data having Price > 15000 and Age < 8 years
price_age_subset = df[(df['Price'] > 15000) & (df['Age'] < 8)]  # Filters by price and age

# d. Merge records of the above two data subsets
merged_subset = pd.merge(petrol_subset, price_age_subset, how='inner')  # Merges both on matching records
