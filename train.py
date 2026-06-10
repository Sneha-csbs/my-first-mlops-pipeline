# train.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1. Get the flower dataset (Textbook)
dataset = load_iris()
X = dataset.data  # The measurements (sepal length, petal width, etc.)
y = dataset.target  # The actual species names (represented as 0, 1, 2)

# 2. Create the blank brain and train it
print("Training the brain...")
brain = RandomForestClassifier()
brain.fit(X, y)  # Learning the patterns

# 3. Save the smart brain to a file
joblib.dump(brain, "smart_brain.pkl")
print("Brain successfully saved as 'smart_brain.pkl'!")