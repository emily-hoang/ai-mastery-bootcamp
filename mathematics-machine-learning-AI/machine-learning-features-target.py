import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/raw/titanic.csv"
data_file = pd.read_csv(url)

features = data_file[['survived', 'name']]
target = data_file['age']

# Print the 5 features, and target in the data file
print("Features: \n", features.head())
print("Target: \n", target.head())

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
# Print the training set of feature (X_train), testing set of features(X_test), y_test, y_train = for training and testing the data set

print("Training data set: ", X_train.shape)
print("Testing data set: ", X_test)

# visualise the relationships
sns.pairplot(data_file, x_vars=["survived", "name"], y_vars='age', height=5, aspect=0.8, kind="scatter")
plt.title("Features vs Target")
plt.show()