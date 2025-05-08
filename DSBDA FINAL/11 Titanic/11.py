# Q11 - Dataset: Titanic-Dataset.csv

# a. Handle missing Age and Cabin values using appropriate imputation techniques
# df = pd.read_csv("Titanic-Dataset.csv")

df['Age'].fillna(df['Age'].median(), inplace=True)  # Fills missing ages with median
df['Cabin'].fillna('Unknown', inplace=True)  # Fills missing cabin entries with 'Unknown'

# b. Convert Sex and Embarked columns into numeric form using encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Sex_encoded'] = le.fit_transform(df['Sex'])  # Encodes Sex as 0/1
df['Embarked_encoded'] = le.fit_transform(df['Embarked'].astype(str))  # Encodes Embarked

# c. Create a new feature FamilySize = SibSp + Parch
df['FamilySize'] = df['SibSp'] + df['Parch']  # Calculates family size

# d. Bin Fare into price categories (e.g., Low, Medium, High)
df['FareCategory'] = pd.qcut(df['Fare'], q=3, labels=['Low', 'Medium', 'High'])  # Bins fare into quantiles
