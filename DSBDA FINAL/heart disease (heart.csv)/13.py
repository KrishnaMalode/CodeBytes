# Q13 - Dataset: heart.csv
# a. Fill missing values in cholesterol, restecg, and thal columns
# df = pd.read_csv("heart.csv")
df['chol'] = df['chol'].fillna(df['chol'].mean())  # Replacing missing cholesterol with column mean
df['restecg'] = df['restecg'].fillna(df['restecg'].mode()[0])  # Using mode for categorical column
df['thal'] = df['thal'].fillna(df['thal'].mode()[0])  # Filling missing values in 'thal' with most frequent

# b. Encode categorical columns like sex, cp, thal using One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['sex', 'cp', 'thal'], drop_first=True)  # One-hot encoding categorical vars

# c. Create an AgeGroup column (young, middle-aged, elderly)
df['AgeGroup'] = pd.cut(df['age'], bins=[0, 40, 60, 100], labels=['young', 'middle-aged', 'elderly'])  # Binning age

# d. Normalize features like chol, thalach, and oldpeak
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['chol', 'thalach', 'oldpeak']] = scaler.fit_transform(df[['chol', 'thalach', 'oldpeak']])  # Min-max normalization

# e. Build a classification model to predict presence of heart disease (target)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))  # Displaying classification metrics
