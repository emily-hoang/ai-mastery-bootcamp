import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic data
# makes results reproducible (same random numbers each run).
np.random.seed(42)
# 100 random numbers between 0 and 10.
X = np.random.rand(100, 1) * 10
# values generated from a quadratic equation
# y=3 * X**2+2 * X + noise The noise (np.random.randn(100, 1) * 5) simulates real-world data imperfections.
y = 3 * X**2 + 2 * X + np.random.randn(100, 1) * 5

# Transform features to polynomial
# Polynomial regression works by expanding your features
# degree=2 means we’re fitting a quadratic model.
# include_bias=False means we don’t add a constant (intercept term) — the regression model will handle that itself.
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Fit Polynomial Regression
# Even though we’re using a linear regression model, the data has been transformed into polynomial form, so it effectively learns a nonlinear curve.
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)

# Plot results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.scatter(X, y_pred, color="red", label="Predicted Data")
plt.title("Polynomial Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Evaluate Model
# MSE (Mean Squared Error) measures how close predictions are to actual values.
# Lower MSE = better fit.
mse = mean_squared_error(y, y_pred)
print("Mean squared error", mse)