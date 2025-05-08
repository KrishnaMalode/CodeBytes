
import pandas as pd

# Load datasets
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# ----- 1. Data Cleaning -----
print("\n--- Data Cleaning ---")
# Fill missing Age with mean
customers['Age'].fillna(customers['Age'].mean(), inplace=True)

# Fix invalid email formats
customers['Email'] = customers['Email'].apply(lambda x: x if '@' in x else 'missing@example.com')

# Standardize city names
customers['City'] = customers['City'].str.title()

# ----- 2. Data Integration -----
print("\n--- Data Integration ---")
# Merge customers with orders on CustomerID
merged_df = pd.merge(customers, orders, on='CustomerID', how='inner')
print(merged_df)

# ----- 3. Data Transformation -----
print("\n--- Data Transformation ---")
# Convert OrderDate to datetime
merged_df['OrderDate'] = pd.to_datetime(merged_df['OrderDate'])

# Create Total Spending per Customer
total_spending = merged_df.groupby('CustomerID')['Amount'].sum().reset_index()
total_spending.columns = ['CustomerID', 'TotalSpending']
print(total_spending)

# ----- 4. Error Correction -----
print("\n--- Error Correction ---")
# Remove any rows with Amount <= 0
merged_df = merged_df[merged_df['Amount'] > 0]

# ----- 5. Optional: Data Model Preparation -----
print("\n--- Add High Value Customer Flag ---")
# Label High Value Customers (e.g., spending > 150)
merged_df = pd.merge(merged_df, total_spending, on='CustomerID')
merged_df['HighValueCustomer'] = (merged_df['TotalSpending'] > 150).astype(int)
print(merged_df[['CustomerID', 'Name', 'TotalSpending', 'HighValueCustomer']].drop_duplicates())
