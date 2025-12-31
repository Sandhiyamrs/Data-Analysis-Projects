from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(100).reshape(50, 2)
y = np.random.randint(0, 2, 50)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Split completed")
