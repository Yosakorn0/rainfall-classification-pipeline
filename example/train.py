import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample training data
X = np.array([[1], [2], [3], [4]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# "Pickle" the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved as model.pkl")
