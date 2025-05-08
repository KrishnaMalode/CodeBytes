# Q24 - Dataset: Toyota.csv
# a. Add a new column ‘Revised’ to the dataset specifying 5% increase in old Price.
df['Revised'] = df['Price'] * 1.05  # Adds 5% increase to the original price

# b. Create subset of cars’ data having Price greater than 15000 and Age less than 8
df_subset = df[(df['Price'] > 15000) & (df['Age'] < 8)]  # Filters based on price and age condition

# c. Sort observations in descending order of Revised Price
df_sorted = df.sort_values(by='Revised', ascending=False)  # Sorts by revised price in descending order

# d. Apply Z-Score normalization on HP column
from scipy.stats import zscore
df['HP_ZScore'] = zscore(df['HP'])  # Applies z-score normalization to HP
