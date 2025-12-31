import joblib
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
joblib.dump(model, "model.pkl")
print("Model saved")
