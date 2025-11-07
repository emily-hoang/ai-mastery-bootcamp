import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Generate Synthetic Data
np.random.seed(42)
X = np.random.randn(100, 1) * 10
y = 3 * X**2 + 2 * X + np.random.randn(100, 1) * 5

# Transform features to polynomial
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

# train_help_split helps you split your dataset into training and testing subsets.
# X → your features (independent variables)
# y → your target (dependent variable)
# test_size → proportion of data used for testing (e.g., 0.2 means 20% test, 80% train)
# train_size → optional; can explicitly set training size instead of test size
# random_state → sets a seed for reproducibility (so you get the same split every time)
# shuffle=True (default) → randomly shuffles data before splitting
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Ridge Regression
ridge_model = Ridge(alpha=1)
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Lasso Regression
lasso_model = Lasso(alpha=1)
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Evaluate Results
# mean_squared_error is a metric function that measures how well the model's predictions match the actual values
# commonly used to evaluate regression models - models that predict continuous values (like house prices, temparatures, or sales)
ridge_mse = mean_squared_error(y_test, ridge_predictions)
lasso_mse = mean_squared_error(y_test, lasso_predictions)

print("Ridge Regression MSE: ", ridge_mse)
print("Lasso Prediction MSE: ", lasso_mse)


