from sklearn.ensemble import IsolationForest
import numpy as np

data = np.array([[10],[12],[11],[13],[100]])
model = IsolationForest(contamination=0.2)
labels = model.fit_predict(data)

anomalies = data[labels == -1]
print("Detected anomalies:", anomalies)
