# CodeAlpha Task 1 - Iris Flower Classification

## Objective

The objective of this task is to classify Iris flowers into three species:

- Setosa
- Versicolor
- Virginica

The classification is performed using flower measurements from the Iris dataset.

## Technologies Used

- Python
- Scikit-learn
- Logistic Regression

## Methodology

1. Load the Iris dataset using Scikit-learn.
2. Split the dataset into training and testing data.
3. Standardize the input features.
4. Train a Logistic Regression classification model.
5. Predict the species of the test samples.
6. Evaluate the model using accuracy, classification report, and confusion matrix.

## Dataset

The Iris dataset is loaded directly from Scikit-learn using `load_iris()`.

## How to Run

Install Scikit-learn:

```bash
pip install scikit-learn