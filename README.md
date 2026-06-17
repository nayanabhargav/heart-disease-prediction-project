# Heart Disease Prediction Using Machine Learning

A machine learning project that predicts the likelihood of heart disease using patient health information. The project uses the Random Forest classification algorithm and evaluates its performance using accuracy, a classification report, and a confusion matrix.

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Flask

## Machine Learning Algorithm

The project uses a **Random Forest Classifier** with 200 decision trees.

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=200)
rf_model.fit(X_train, y_train)
```

## Project Workflow

1. Load the heart disease dataset.
2. Inspect and clean the data.
3. Select the input features and target variable.
4. Split the dataset into training and testing sets.
5. Train the Random Forest classifier.
6. Predict results on the test dataset.
7. Evaluate the model using accuracy, classification report, and confusion matrix.

## Results

* Achieved approximately **89% accuracy** on the test dataset.
* Evaluated performance using precision, recall, F1-score, and confusion matrix.

## Repository Files

* `heart_disease_prediction.ipynb` – Data preprocessing, model training, prediction, and evaluation
* `heart.xls` – Dataset used for the project
* `app.py` – Flask web application
* `requirements.txt` – Required Python libraries
* `Procfile` – Deployment configuration

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/nayanabhargav/heart-disease-prediction-project.git
```

2. Open the project folder:

```bash
cd heart-disease-prediction-project
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook heart_disease_prediction.ipynb
```

## Author

**Nayana B**

MCA Candidate | Aspiring Data Analyst and AI/ML Engineer
