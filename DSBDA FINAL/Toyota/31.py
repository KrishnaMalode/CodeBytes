# Q31 - Dataset: Toyota.csv
# df = pd.read_csv("Toyota.csv")

import matplotlib.pyplot as plt

# a. Age vs Price - Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Price'], color='teal')
plt.title('Age vs Price Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# b. Distribution of KM data - histogram
plt.figure(figsize=(8, 6))
plt.hist(df['KM'], bins=25, color='salmon', edgecolor='black')
plt.title('Histogram of KM Driven')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# c. FuelType wise Cars Count - Barplot
fuel_counts = df['FuelType'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(fuel_counts.index, fuel_counts.values, color=['blue', 'gray', 'gold'])
plt.title('Fuel Type Car Counts')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.grid(True)
plt.show()
