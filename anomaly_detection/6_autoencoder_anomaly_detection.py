import numpy as np
from sklearn.neural_network import MLPRegressor

X = np.random.normal(0, 1, (100, 2))
autoencoder = MLPRegressor(hidden_layer_sizes=(2,), max_iter=500)

autoencoder.fit(X, X)
recon = autoencoder.predict(X)

error = np.mean((X - recon) ** 2, axis=1)
print("Reconstruction error:", error[:5])
