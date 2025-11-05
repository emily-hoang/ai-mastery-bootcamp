import sympy as sp

# Define a multi variable function
x, y = sp.symbols('x y')
f = x**2 + 3*y*2 - 4*x*y

# Compute partial derivatives
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Gradients: ")
print("Gradient X: ", grad_x)
print("Gradient Y: ", grad_y)