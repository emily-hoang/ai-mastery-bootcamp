import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
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

# Fit Polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Make Predictions
y_pred = model.predict(X_poly)

# Plot actual vs predicted values
plt.figure(figsize=(10,6))
plt.scatter(X, y, color="blue", label="Actual Data", alpha=0.5)
plt.scatter(X, y_pred, color="red", label="Predicted Curve", alpha=0.5)
plt.title("Polynomial Regression")
plt.xlabel("Median Income in California")
plt.ylabel("Median House Value in Califonia")
plt.legend()
plt.show()

# Evaluate model performance
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error: ", mse)