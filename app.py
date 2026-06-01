import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    """
    <style>
    .app-container {max-width: 800px; margin: auto;}
    .card {background: #ffffff; border: 1px solid #e6e6e9; border-radius: 20px; padding: 32px; box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);}
    .field-card {background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 18px; padding: 22px;}
    .title {font-size: 2.4rem; font-weight: 700; margin-bottom: 6px;}
    .subtitle {color: #475569; margin-bottom: 24px;}
    .footer {color: #64748b; text-align: center; padding-top: 18px;}
    .button-row button {width: 100%; height: 3.4rem; font-size: 1.05rem; border-radius: 14px;}
    @media (max-width: 640px) {
        .card {padding: 24px;}
        .field-card {padding: 18px;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

MODEL_PATH = Path(__file__).parent / "student_model.pkl"

st.markdown("<div class='app-container'>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🎓 Student Performance Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Predict student scores using Machine Learning.</div>", unsafe_allow_html=True)

if not MODEL_PATH.exists():
    st.error(
        "The trained model file `student_model.pkl` is missing. "
        "Run `python train_model.py` first to generate the model."
    )
    st.stop()

with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

with st.form(key="prediction_form"):
    st.markdown("<div class='field-card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=4.0,
            step=0.5,
            help="Average daily study time in hours.",
        )
    with col2:
        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=85.0,
            step=1.0,
            help="Attendance percentage in class.",
        )

    previous_marks = st.number_input(
        "Previous Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0,
        help="Marks obtained in the previous exam.",
    )

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
    with button_col2:
        submit_button = st.form_submit_button("Predict Score")

    st.write("")

if submit_button:
    if attendance < 0 or attendance > 100:
        st.error("Attendance must be between 0 and 100 percent.")
    elif previous_marks < 0 or previous_marks > 100:
        st.error("Previous marks must be between 0 and 100.")
    elif study_hours < 0 or study_hours > 24:
        st.error("Study hours must be between 0 and 24.")
    else:
        input_df = pd.DataFrame(
            [[study_hours, attendance, previous_marks]],
            columns=["StudyHours", "Attendance", "PreviousMarks"],
        )
        prediction = model.predict(input_df)
        predicted_score = float(prediction[0])

        st.success(f"✅ Predicted Score: {predicted_score:.2f}")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Developed by Ramesh</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
