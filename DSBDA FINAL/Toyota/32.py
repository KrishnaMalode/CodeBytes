# Q32 - Dataset: Toyota.csv
# df = pd.read_csv("Toyota.csv")

import seaborn as sns
import matplotlib.pyplot as plt

# a. Age vs Price - Scatter plot using seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Price', hue='FuelType')
plt.title('Age vs Price by Fuel Type')
plt.xlabel('Age')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# b. Distribution of KM data - histogram using seaborn
plt.figure(figsize=(8, 6))
sns.histplot(df['KM'], bins=30, kde=True, color='darkgreen')
plt.title('KM Distribution')
plt.xlabel('KM')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# c. FuelType wise Cars Count - Barplot using seaborn
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='FuelType', palette='pastel')
plt.title('Car Count by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.grid(True)
plt.show()
