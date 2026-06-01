import pandas as pd
import pickle

# Load model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# User Inputs
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))
previous_marks = float(input("Enter Previous Marks: "))

# Input Data
input_data = pd.DataFrame(
    [[study_hours, attendance, previous_marks]],
    columns=["StudyHours", "Attendance", "PreviousMarks"]
)

# Prediction
prediction = model.predict(input_data)

print(f"\nPredicted Score: {prediction[0]:.2f}")