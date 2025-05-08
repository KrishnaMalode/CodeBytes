# a. Create data subset selecting Ozone, Solar.R, Wind, Temp and specific index range
subset_cols = df.loc[0:30, ['Ozone', 'Solar.R', 'Wind', 'Temp']]  # Subset with specific columns and row index range

# b. Rationally Replace NaN values
df_filled = df.fillna(method='ffill')  # Forward fill to replace missing values

# c. Apply Min-Max Normalization on Solar.R
df['Solar.R_norm'] = (df['Solar.R'] - df['Solar.R'].min()) / (df['Solar.R'].max() - df['Solar.R'].min())

# d. Plot Month-wise Temperature using Matplotlib / Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x='Month', y='Temp', data=df)  # Boxplot to show temperature distribution by Month
plt.title("Month-wise Temperature Distribution")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.show()
