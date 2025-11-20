import pandas as pd
# Feature engineering in machine learning is the process of creating, selecting, transforming, and improving the input variables (features) used to train a model.
titanic_raw_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/raw/titanic.csv"
df = pd.read_csv(titanic_raw_data)

# Display the dataset info and preview the first 5 rows
print("Dataset Info: \n", df.info())
print("First 5 rows: \n", df.head())

categorical_features = df.select_dtypes(include=["object"]).columns
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns
# Display categorical features and numerical features
# Categorical Features:  ['name', 'sex', 'ticket', 'cabin', 'embarked']
# Numerical Features:  ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
print("Categorical Features: ", categorical_features.tolist())
print("Numerical Features: ", numerical_features.tolist())

# Display summary of categorical features
print("Categorical Features Summary: \n")
for col in categorical_features:
  print(f"{col}:\n", df[col].value_counts(), "\n")

# Display summary of numerical features
print("Numerical Features Summary: \n")
print(df[numerical_features].describe())