
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
df = sns.load_dataset('titanic')

# Set style
sns.set(style="whitegrid")

# 1. Bar plot of survival rate by gender
plt.figure(figsize=(6,4))
sns.barplot(x='sex', y='survived', data=df)
plt.title('Survival Rate by Gender')
plt.savefig('barplot_survival_by_gender.png')
plt.close()

# 2. Histogram of passenger age
plt.figure(figsize=(6,4))
sns.histplot(data=df, x='age', hue='survived', bins=30, kde=True)
plt.title('Age Distribution by Survival Status')
plt.savefig('histogram_age_survival.png')
plt.close()

# 3. Heatmap of correlation matrix
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.savefig('heatmap_correlations.png')
plt.close()

# 4. Boxplot of Fare by Passenger Class
plt.figure(figsize=(6,4))
sns.boxplot(x='pclass', y='fare', data=df)
plt.title('Fare Distribution by Passenger Class')
plt.savefig('boxplot_fare_pclass.png')
plt.close()

# 5. Countplot of embarkation ports
plt.figure(figsize=(6,4))
sns.countplot(x='embarked', data=df)
plt.title('Passenger Count by Embarkation Port')
plt.savefig('countplot_embarked.png')
plt.close()

print("All plots saved as PNG files.")
