import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

def load_data():
    # Load the Diabetes dataset and return features and target values.   
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    print("Data features \n", diabetes.feature_names)
    return X, y

def split_data(X, y):
    # Split the data into training and testing sets.    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
    return X_train, X_test, y_train, y_test