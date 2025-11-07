import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error

# Load the Canifornia housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame
# print ("California Data: ", df)

# Select feature (Median Income) and target (Median Housing Value)
X = df[["MedInc"]]
y = df[["MedHouseVal"]]

# Transform feature to Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Ridge regression model
ridge_model = Ridge(alpha=1)
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Lasso regression model
lasso_model = Ridge(alpha=1)
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Plot actual vs predicted values
plt.figure(figsize=(10,6))
plt.scatter(X_test[:, 0], y_test, color="blue", label="Actual Data", alpha=0.5)
plt.scatter(X_test[:, 0], ridge_predictions, color="black", label="Ridge Predictions", alpha=0.5)
plt.scatter(X_test[:, 0], lasso_predictions, color="green", label="Lasso Predictions", alpha=0.5)
plt.title("Ridge vs Lasso Regression")
plt.xlabel("Median Income (Transformed)")
plt.ylabel("Median House Value in Califonia")
plt.legend()
plt.show()

# Evaluate model performance
ridge_mse = mean_squared_error(y, ridge_predictions)
print("Ridge Mean Squared Error: ", ridge_mse)

lasso_mse = mean_squared_error(y, lasso_predictions)
print("Lasso Mean Squared Error: ", lasso_mse)