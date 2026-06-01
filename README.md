# Student Performance Predictor

A polished Python machine learning project that predicts student performance using a trained regression model. This project includes training, inference, and a Streamlit web application suitable for internship or portfolio presentations.

## Project Contents

- `data.csv` - dataset containing the training records
- `train_model.py` - training script that builds and saves `student_model.pkl`
- `student_model.pkl` - serialized trained model used by the Streamlit app
- `predict.py` - console-based prediction script
- `app.py` - Streamlit web application for interactive score prediction
- `requirements.txt` - project dependencies

## Dataset Columns

- `StudyHours`
- `Attendance`
- `PreviousMarks`
- `Score`

## Local Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

- Windows:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Train the model (creates `student_model.pkl`):

```bash
python train_model.py
```

5. Run the Streamlit app:

```bash
streamlit run app.py
```

## Streamlit Cloud Deployment

1. Push the project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in.
3. Click **New app** and connect your GitHub repository.
4. Set the main file to `app.py`.
5. Deploy the app and wait for the build to finish.

## Usage

- Enter realistic values for study hours, attendance, and previous marks.
- Click **Predict Score** to see the estimated student score.
- Use the sidebar to review project details and feature definitions.

## Notes

- The app loads the trained model from `student_model.pkl`.
- Input validation ensures values are within sensible ranges.
- The UI is designed for a professional project demo.
