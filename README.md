# 🧑‍💼 Employee Attrition Prediction Web App

## 📌 About the Project
This project is a **Machine Learning-powered Flask web application** that predicts whether an employee is **likely to leave** or **stay** in a company based on certain key features.

It also:
- Uses a **simplified ML model** trained on only **5 important features**.
- Stores **user inputs and predictions** directly into a **MySQL database**.
- Has a **beautiful CSS UI** with animations, gradients, shadows, and modern styles.
  

## 🚀 Features
- **Simple Input Form** → Only 5 fields needed:
  1. Monthly Income  
  2. Age  
  3. Total Working Years  
  4. Daily Rate  
  5. Years At Company
- **Prediction** → Random Forest Classifier trained on real attrition data.
- **Database Storage** → All inputs and predictions saved to MySQL (`attrition_records` table).
- **Modern UI** → Uses gradient backgrounds, animated buttons, glassmorphism effects.
- **Instant Results** → See prediction immediately after submission.


## 🛠️ Technologies Used
- **Python 3**
- **Flask**
- **scikit-learn**
- **NumPy**
- **MySQL (via flask-mysqldb)**
- **HTML / CSS / Bootstrap**
- **Pickle** for model serialization


## 🚀 Future Improvements

- **Cloud Deployment:** Host the app and database on platforms like AWS or Azure for better scalability and global access.
- **User Authentication:** Add user login and role-based access to secure data and manage predictions per user.
- **Advanced Analytics:** Incorporate visual dashboards and model explainability tools (like SHAP or LIME) for deeper insights.
