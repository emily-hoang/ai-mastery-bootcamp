from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
rs = RandomState(MT19937(SeedSequence(123456789)))
# Later, you want to restart the stream
rs = RandomState(MT19937(SeedSequence(987654321)))
n_samples = 200
X = rs.rand(n_samples, 2) * 10

# This defines the label rule.
# If 1.5 × Age + Salary > 15, the label is 1 (e.g., “Purchase”).
# Otherwise, it’s 0 (no purchase).
y = (X[:, 0] * 1.5 + X[:, 1] > 15).astype(int)

# Create a Dataframe
df = pd.DataFrame(X, columns=['Age', 'Salary'])
df['Purchase'] = y
# Age  | Salary | Purchase
# 3.45 | 7.81   | 0
# 8.12 | 6.57   | 1


# Split Data
X_train, X_test, y_train, y_test = train_test_split(df[['Age', 'Salary']], df['Purchase'], test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make prediction
y_predict = model.predict(X_test)

# Evaluate performance
# % of total correct predictions.
print("Accuracy: ", accuracy_score(y_test, y_predict))
# how many predicted positives are actually positive.
print("Precision: ", precision_score(y_test, y_predict))
# how many actual positives were identified correctly.
print("Recall: ", recall_score(y_test, y_predict))
# harmonic mean of precision and recall.
print("F1 Score: ", f1_score(y_test, y_predict))
# summary of all these metrics.
print("Classification Report: \n", classification_report(y_test, y_predict))

# Plot decision boundary
# Creates a grid of (Age, Salary) values covering the whole space.
# The grid is used to visualize what class the model predicts at each coordinate.
x_min, x_max = X[:, 0].min() - 1, X[:, 1].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Predict probabilities for grid points
# combines the grid points into a 2D array for prediction.
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# Z contains the predicted class (0 or 1) for each point.
# reshape makes Z match the grid’s shape so it can be plotted.
Z = Z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, Z, alpha=0.8, cmap="coolwarm")
plt.scatter(X_test['Age'], X_test['Salary'], c=y_test, edgecolor="k", cmap="coolwarm")
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()