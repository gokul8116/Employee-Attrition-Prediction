from flask import Flask, render_template, request
import pickle
import numpy as np
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations - note the custom port 3307
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'   # replace with your MySQL user
app.config['MYSQL_PASSWORD'] = 'root'   # replace with your password
app.config['MYSQL_DB'] = 'employee_attrition'
app.config['MYSQL_PORT'] = 3307  # specify your port here

mysql = MySQL(app)

# Load your trained model
model = pickle.load(open("./ML Model/attrition_model.pkl", "rb"))

feature_columns = [
    "MonthlyIncome",
    "Age",
    "TotalWorkingYears",
    "DailyRate",
    "YearsAtCompany"
]

@app.route('/')
def home():
    return render_template("index.html", feature_columns=feature_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        features = [float(request.form[col]) for col in feature_columns]
        final_features = [np.array(features)]

        # Make prediction
        prediction_num = model.predict(final_features)[0]
        result = "LIKELY to leave" if prediction_num == 1 else "NOT likely to leave"

        # Store input and output in MySQL database
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO attrition_records (MonthlyIncome, Age, TotalWorkingYears, DailyRate, YearsAtCompany, prediction) VALUES (%s, %s, %s, %s, %s, %s)",
            (*features, result)
        )
        mysql.connection.commit()
        cur.close()

        return render_template("result.html", prediction_text=f"The employee is {result}.")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
