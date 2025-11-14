from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
data = load_iris()
X, y = data.data, data.target

# Initialize the Random Forest Classifier
model = RandomForestClassifier(random_state=42)

# Perform K-Fold cross-validation
# K-Fold cross-validation is a resampling technique used to evaluate the performance of a machine learning model. It splits the dataset into K subsets (folds) of approximately equal size. The model is trained on K-1 folds and tested on the remaining fold. This process is repeated K times, with each fold being used as the test set exactly once. The final performance metric is the average of the scores obtained in each iteration.
# n_splits=5: The dataset is divided into 5 folds.
# shuffle=True: The data is shuffled before splitting to ensure randomness.
# random_state=42: Ensures reproducibility of the shuffle.
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# The scores array contains the accuracy for each fold. For example:
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

# Print the accuracy for each fold and the average accuracy
print("Cross-validation scores for each fold: ", scores)
print("Mean Accuracy: ", scores.mean())

# Summary:
# Reduces Overfitting: By training and testing on different subsets, it ensures the model generalizes well.
# Efficient Use of Data: All data points are used for both training and testing, maximizing the utility of the dataset.
# Reproducibility: The random_state ensures consistent results across runs.