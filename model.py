# Import libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Convert target
labels = {0 : 'iris-setosa',
          1 : 'iris-versicolor',
          2 : 'iris-virginica'}
y = np.vectorize(labels.__getitem__)(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create classifier
rf = RandomForestClassifier(random_state=42)

# Train classifier
rf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = rf.predict(X_test)

# Print accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save trained model
joblib.dump(rf, 'model.pkl')
print("Model saved to model.pkl")