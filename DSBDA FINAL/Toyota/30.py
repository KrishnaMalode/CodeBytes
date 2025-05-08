# Q30 - Dataset: Toyota.csv
# df = pd.read_csv("Toyota.csv")

import matplotlib.pyplot as plt
import seaborn as sns

# a. Scatter plot - Car Price by Age
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Price'], color='blue')  # Plots Age on x-axis and Price on y-axis
plt.title('Car Price by Age')
plt.xlabel('Age')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# b. Histogram on Cars data KM
plt.figure(figsize=(8, 6))
plt.hist(df['KM'], bins=30, color='orange', edgecolor='black')  # Creates histogram for KM column
plt.title('Distribution of KM')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# c. Bar plot on counts of FuelType category (Petrol, Diesel, and CNG)
fuel_counts = df['FuelType'].value_counts()  # Counts the occurrences of each FuelType
plt.figure(figsize=(8, 6))
fuel_counts.plot(kind='bar', color=['green', 'red', 'purple'])  # Bar chart for FuelType count
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.grid(True)
plt.show()
