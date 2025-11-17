import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load Telco Customer Churn dataset
df_telco = pd.read_csv("https://raw.githubusercontent.com/arya-io/telco-customer-churn-eda/refs/heads/main/Customer_Churn.csv")

# Inspect the first few rows of the Telco dataset
print("First 5 rows of Telco dataset: ", df_telco.head())
print("Missing values in each column of Telco dataset:\n", df_telco.isnull().sum())

# Visualise the relationship between features and target in Telco dataset
label_encoder = LabelEncoder()
df_telco['Churn'] = label_encoder.fit_transform(df_telco['Churn'])
sns.countplot(x='Churn', data=df_telco)
plt.title("Customer Churn Distribution")
plt.show()

# Define features and target
X = df_telco.drop(columns=['Churn'])
y = df_telco['Churn']

# Scale Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train logistic regression model
logistic_model = LogisticRegression(max_iter=200)
# The fit() function is a core method in machine learning models, including the LogisticRegression class from scikit-learn. Its purpose is to train the model on the given dataset by learning the optimal parameters (e.g., weights and biases) that minimize the error for the task at hand.
logistic_model.fit(X_train, y_train)

# Train k-NN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Evaluate the models
logistic_model_pred = logistic_model.predict(X_test)
knn_model_pred = knn_model.predict(X_test)

# Print model accuracies
logistic_report = classification_report(y_test, logistic_model_pred, )
knn_report = classification_report(y_test, knn_model_pred)

print("Logistic Regression Classification Report:\n", logistic_report)
print("k-NN Classification Report:\n", knn_report)