# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load the dataset
print("Loading diabetes dataset...")
diabetes = load_diabetes()

# Convert to DataFrame for easier viewing (optional)
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.Series(diabetes.target, name='progression')

print(f"\nDataset shape: {X.shape}")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")


# Split: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Model Training
model = RandomForestRegressor(
    n_estimators=100,      # Number of trees
    max_depth=5,           # Limit tree depth
    random_state=42
)

model.fit(X_train, y_train)
print("✓ Model training complete!")

# Make Predictions
# Predict on test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nPerformance Metrics:")
print(f"R² Score: {r2:.4f} ({r2*100:.2f}% variance explained)")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
