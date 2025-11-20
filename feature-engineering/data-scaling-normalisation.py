from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Load dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train k-NN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)

print("Accuracy with KNN Classifier: ", accuracy_score(y_test, y_pred))

# Apply Min-Max Scaling 
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_scaled_train, X_scaled_test, y_scaled_train, y_scaled_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_scaled_train, y_scaled_train)

y_scaled_pred = knn_scaled.predict(X_scaled_test)
print("Accuracy with KNN Classifier with Min-Max Scaling: ", accuracy_score(y_scaled_test, y_scaled_pred))

# Apply Standard Scaling
standard_scaler = StandardScaler()
X_standard_scaled = standard_scaler.fit_transform(X)

X_standard_scaled_train, X_standard_scaled_test, y_standard_scaled_train, y_standard_scaled_test = train_test_split(X_standard_scaled, y, test_size=0.2, random_state=42)

knn_standard_scaled = KNeighborsClassifier(n_neighbors=5)
knn_standard_scaled.fit(X_standard_scaled_train, y_standard_scaled_train)

y_standard_scaled_pred = knn_standard_scaled.predict(X_standard_scaled_test)
print("Accuracy with KNN Classifier with Standard Scaling: ", accuracy_score(y_standard_scaled_test, y_standard_scaled_pred))