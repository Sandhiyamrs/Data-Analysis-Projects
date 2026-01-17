import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

df = pd.read_csv("dataset1.csv")

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df)

input_dim = X_scaled.shape[1]
input_layer = Input(shape=(input_dim,))
encoded = Dense(8, activation="relu")(input_layer)
decoded = Dense(input_dim, activation="sigmoid")(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer="adam", loss="mse")

autoencoder.fit(
    X_scaled, X_scaled,
    epochs=50,
    batch_size=32,
    verbose=0
)

reconstructions = autoencoder.predict(X_scaled)
reconstruction_error = np.mean(
    np.square(X_scaled - reconstructions), axis=1
)

threshold = np.percentile(reconstruction_error, 95)
anomalies = df[reconstruction_error > threshold]

print(anomalies)
