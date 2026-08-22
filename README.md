# Student Performance Prediction

A machine learning project that predicts students' final Mathematics grades (`G3`) using their first-period (`G1`) and second-period (`G2`) grades.

## Project Overview

This project uses the Student Performance dataset to build a simple regression model for predicting a student's final grade.

The workflow includes:

1. Loading the Mathematics and Portuguese datasets.
2. Exploring the dataset structure.
3. Selecting `G1` and `G2` as input features.
4. Using `G3` as the target variable.
5. Splitting the data into training and testing sets.
6. Training a linear regression model.
7. Evaluating the model using R² Score and Mean Squared Error.
8. Comparing actual and predicted final grades with a scatter plot.
9. Making a prediction for a new set of grades.

## Dataset

The project uses two CSV files:

- `Maths.csv` — Mathematics student performance data.
- `Portuguese.csv` — Portuguese student performance data.

The Mathematics dataset contains **397 students** and **33 columns**.

Important columns used in this project:

| Column | Description |
|---|---|
| `G1` | First-period grade |
| `G2` | Second-period grade |
| `G3` | Final grade |

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Machine Learning

### Input Features

The model uses:

```text
G1
G2
```

### Target

The model predicts:

```text
G3
```

### Train/Test Split

The dataset was split into:

- **80% training data** — 317 records
- **20% testing data** — 80 records

The split used:

```python
train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=20
)
```

## Model Performance

The trained model achieved:

**R² Score: 0.8478**

This means the model explains approximately **84.78% of the variation** in the final grades for the test data.

The Mean Squared Error obtained during testing was approximately:

**1.1042**

## Actual vs Predicted Grades

The following graph compares the students' actual final grades (`G3`) with the grades predicted by the model.

> **Add your graph screenshot here.**

Save your screenshot in the repository, for example:

```text
images/actual-vs-predicted.png
```

Then use this Markdown:

```markdown
![Actual vs Predicted Final Grades](images/actual-vs-predicted.png)
```

### Graph

![Actual vs Predicted Final Grades](images/actual-vs-predicted.png)

The points show that the predicted grades generally follow the actual `G3` values. The closer the points are to a straight diagonal relationship, the better the predictions match the actual grades.

## Example Prediction

The model was also used to predict a final grade from input grades.

Example predicted final grade:

```text
13.768157430003765
```

This can be rounded for presentation:

```text
13.77
```

## Project Structure

```text
Predict-Student-Performance/
│
├── Maths.csv
├── Portuguese.csv
├── student_performance.py
├── README.md
└── images/
    └── actual-vs-predicted.png
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Predict-Student-Performance
```

### 2. Install the required libraries

```bash
pip install pandas scikit-learn matplotlib openpyxl
```

### 3. Run the Python program

```bash
python student_performance.py
```

The program will load the dataset, train the model, display the evaluation results, and generate the actual-vs-predicted graph.

## Key Learning Outcomes

Through this project, I practiced:

- Loading datasets with Pandas
- Exploring DataFrame structure
- Selecting features and target variables
- Splitting data into training and testing sets
- Building a machine learning regression model
- Evaluating model performance
- Making predictions
- Creating data visualizations with Matplotlib

## Results

The project demonstrates that `G1` and `G2` grades can be useful features for estimating a student's final `G3` grade. The achieved R² score of **0.8478** indicates a strong relationship between the model's predictions and the actual final grades in this test split.

## Author

**Rames**

Student Performance Prediction — Internship Final Assessment
