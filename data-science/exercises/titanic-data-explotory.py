import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
data = pd.read_csv(url)

print("=========TITANIC DATA INFO=======: \n", data.info())
print("=========DESCRIBING TITANIC DATA=====: \n", data.describe())

# TASK 1: DATA CLEANING, AGGREGATION, FILTERING
# Fill missing age with the everage age
data["Age"] = data["Age"].fillna(data["Age"].median())
# Fill missing value for embarked with False
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
# Remove duplications
data = data.drop_duplicates()
# Filter data: Passenger in first class
first_class = data[data["Pclass"] == 1]
print("=======5 FIRST CLASS PASSENGERS=========: \n", first_class.head())

# TASK 2: KEY INSIGHTS VISUALISATIONS
# Bar chart: Survival Rate By Class
survival_by_class = data.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate By Class")
plt.show()

# Histogram: Age Distribution
sns.histplot(data["Age"], kde=True, bins=20, color="skyblue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Age vs Fare
plt.scatter(data["Age"], data["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# TASK 3: INDENTIFY & INTERPRET PATTERNS OR ANOMALIES
