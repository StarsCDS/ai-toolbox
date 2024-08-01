import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 1000
tenure_months = np.random.randint(1, 60, size=n_samples)
feature1 = np.random.randn(n_samples)  # Example feature 1
feature2 = np.random.randn(n_samples)  # Example feature 2
churn = np.random.randint(0, 2, size=n_samples)  # Binary target variable

# Create a DataFrame
data = pd.DataFrame({
    'tenure_months': tenure_months,
    'feature1': feature1,
    'feature2': feature2,
    'churn': churn
})

# Save the synthetic data to a CSV file
data.to_csv('customer_data.csv', index=False)

# Example: Simple DataOps pipeline for ML model training
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data ingestion
data = pd.read_csv('customer_data.csv')

# Data preprocessing
X = data.drop('churn', axis=1)
y = data['churn']

# Data quality check
assert X.isnull().sum().sum() == 0, "Missing values detected"

# Feature engineering
X['tenure_years'] = X['tenure_months'] / 12

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Model evaluation
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Monitoring
if accuracy < 0.8:
    print("Warning: Model performance below threshold")

# Version control and logging (placeholder)
print("Logging model version and performance metrics...")