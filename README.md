🧠** Predictive Pulse: Harnessing Machine Learning for Blood Pressure Analysis
📘 Project Overview**
Hypertension (high blood pressure) is one of the leading risk factors for cardiovascular diseases worldwide. Early prediction of hypertension based on lifestyle and medical data can help individuals take preventive measures and enable healthcare providers to offer timely interventions.
This project, Predictive Pulse, uses Machine Learning to predict whether a person is likely to have hypertension, based on medical and demographic factors. It also includes a Flask web app where users can input their health details and get predictions instantly.
🎯** Objectives**
To preprocess and clean raw health data for model training.
To explore patterns and correlations between key factors and hypertension.
To train and evaluate multiple ML models for prediction accuracy.
To deploy a user-friendly web interface using Flask.

**🧩 Dataset**
Source: patient_data.csv (from kaggle).
**Files used:**
data_cleaned.csv – Preprocessed dataset used for training and testing models.
model.pkl – Serialized trained model file for deployment.
data.json – Supporting metadata for the model.

**Sample Features:**
Age
Gender
Smoking habits
Alcohol intake
BMI
Physical activity level
Family history of hypertension
Cholesterol level

⚙️ **Technologies Used**
Category	Tools / Libraries
Programming Language	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Model Deployment	Flask
Version Control	Git & GitHub
Hosting	Render

🧠** Machine Learning Models Implemented**
The following algorithms were trained and compared:
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Gaussian Naive Bayes
Multinomial Naive Bayes

**Evaluation Metrics:**
Accuracy
Precision
Recall
F1-Score

After model comparison, the Random Forest Classifier achieved the highest accuracy and was selected for deployment.

🧮 **Project Workflow**
Data Loading: Imported CSV and cleaned null or invalid values.
Data Preprocessing: Encoded categorical variables and handled missing data using SimpleImputer.
EDA: Visualized trends in hypertension risk factors using heatmaps, pair plots, and bar charts.
Model Training: Trained ML models using train-test split.
Model Evaluation: Compared performance metrics and selected the best model.
Model Saving: Serialized the trained model using pickle.

**Deployment**: Built a Flask web app to provide real-time prediction
