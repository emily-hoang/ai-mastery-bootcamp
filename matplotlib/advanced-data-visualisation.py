# Seaborn is a powerful data visualization library in Python built on top of Matplotlib. 
# It provides a high-level interface for creating beautiful, informative, and statistically meaningful visualizations with less code than raw Matplotlib.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heat Map")
plt.show()

# A pairplot() is great for visualizing relationships between multiple numerical columns, often colored by a categorical column.
# Diagonal: Histograms for each numeric column (Height, Weight, Age)
# Off-diagonal: Scatter plots showing pairwise relationships
# Colors: Points are colored by Gender
data = pd.DataFrame({
    'Height': [150, 160, 165, 170, 175, 180, 185, 190],
    'Weight': [50, 55, 60, 65, 70, 75, 80, 85],
    'Age': [22, 25, 23, 30, 35, 32, 38, 40],
    'Gender': ['Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male']
})
sns.pairplot(data, hue='Gender', kind='reg')   # Add regression lines
sns.pairplot(data, hue='Gender', markers=['o', 's'])
plt.title("Pair Plot")
plt.show()

