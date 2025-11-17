from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import precision_score, accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load Iris dataset
data = load_iris()
X, y = data.data, data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Experiment with different values of k
for k in range(1, 11):
  # Initialise k-NN model
  model = KNeighborsClassifier(n_neighbors=k)
  model.fit(X_train, y_train)
  
  # Predict on the test set
  y_pred = model.predict(X_test)
  
  # Evaluate model's performance
  accuracy = accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred, average='weighted')
  f1_scores = f1_score(y_test, y_pred, average='weighted')
  confusion_matrix_value = confusion_matrix(y_test, y_pred)
  
  # uses an f-string to format the output dynamically. Here's what it does:
  # f"k={k}": The f prefix indicates an f-string, which allows embedding expressions inside curly braces {}. Here, the value of the variable k is inserted into the string.
  # Accuracy={accuracy:.4f}: The value of the variable accuracy is formatted to 4 decimal places using :.4f.
  # Precision={precision:.4f}: Similarly, the value of precision is formatted to 4 decimal places.
# F1-Score={f1_score:.4f}: The value of f1_score is also formatted to 4 decimal places.
  print(f"k={k}: Accuracy={accuracy:.4f}, Precision={precision:.4f}, F1-Score={f1_scores:.4f}, Confusion Matrix=\n{confusion_matrix_value}\n")
  