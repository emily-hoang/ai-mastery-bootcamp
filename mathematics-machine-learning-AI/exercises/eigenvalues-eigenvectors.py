import numpy as np
import matplotlib.pyplot as plt

# Define a 2x2 matrix
A = np.array([[2, 1],
              [1, 2]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Plot the original eigenvectors and their scaled versions
origin = np.array([[0, 0], [0, 0]])  # origin point for vectors

# Original eigenvectors
vecs = eigenvectors.T  # make it easier to plot
scaled_vecs = (eigenvalues * vecs.T).T  # scale by eigenvalues

plt.figure(figsize=(6, 6))
plt.quiver(*origin, vecs[:, 0], vecs[:, 1], color=['blue', 'green'], angles='xy', scale_units='xy', scale=1, label='Eigenvectors')
plt.quiver(*origin, scaled_vecs[:, 0], scaled_vecs[:, 1], color=['cyan', 'lime'], angles='xy', scale_units='xy', scale=1, label='Transformed Eigenvectors')

# Formatting
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.title("Eigenvectors and Their Transformations by Matrix A")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(['Eigenvector 1', 'Eigenvector 2', 'Transformed v1', 'Transformed v2'])
plt.show()
