import sympy as sp

# A derivative in calculus measures how fast something is changing at a given point.
# Imagine you're riding a bike uphill.
# Your height changes with distance → that's like a function.
# How steep the hill is at each point → that's the derivative.

# Ex 1: Compute derivatives of basic functions
x = sp.Symbol('x')
f = x**3 - 5*x + 7

# Compute Derivative
derivative = sp.diff(f, x)

print("Function: ", f)
print("Derivative: ", derivative)