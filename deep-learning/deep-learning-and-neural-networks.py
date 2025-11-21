from tensorflow.keras.datasets import mnist, cifar10
import tensorflow as tf
import matplotlib.pyplot as plt
import torch.nn as nn


# Load MNIST dataset
(mnist_X_train, mnist_y_train), (mnist_X_test, mnist_y_test) = mnist.load_data()
print(f"MNIST Dataset: Train - {mnist_X_train.shape}, Test - {mnist_X_test.shape}")

# Load CIFAR-10
(cifar_X_train, cifar_y_train), (cifar_X_test, cifar_y_test) = cifar10.load_data()
print(f"CIFAR-10 Dataset: Train - {cifar_X_train.shape}, Test - {cifar_X_test.shape}")

# Define a basic dense layer
layer = tf.keras.layers.Dense(units=10, activation='relu')
print(f"Tensorflow layer: {layer}")

pytorch_layer = nn.Linear(in_features=10, out_features=5)
print(f"Pytorch layer: {pytorch_layer}")

# Visualise CIFAR-10 sample
plt.imshow(cifar_X_train[0], cmap="gray")
plt.title(f"CIRFAR-10 label: {cifar_y_train[0]}")
plt.show()

# Visualise MNIST sample
plt.imshow(mnist_X_train[0])
plt.title(f"MNIST label: {mnist_y_train[0]}")
plt.show()