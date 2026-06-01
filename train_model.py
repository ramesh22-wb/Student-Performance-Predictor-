# Train a student performance prediction model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Last column target ani assume chestunnam
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
score = r2_score(y_test, y_pred)
print(f"Model Accuracy (R² Score): {score:.2f}")

# Save Model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")
print("Model saved as student_model.pkl")