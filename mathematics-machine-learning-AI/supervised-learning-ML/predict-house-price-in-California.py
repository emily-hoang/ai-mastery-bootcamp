from sklearn.datasets import fetch_california_housing
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = fetch_california_housing(as_frame=True)
df = data.frame
missing_values = df.isnull().sum()

# Inspecct the first few rows of the dataset
print("First 5 rows: ", df.head())
print("Missing values in each column:\n", missing_values)

# Visualise the relationship between features and target
sns.pairplot(df, x_vars=df.columns[:-1], y_vars='MedHouseVal', height=4, aspect=0.8, kind="scatter")
plt.show()