import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the system metrics dataset from CSV
df = pd.read_csv('system_metrics.csv')

# Select CPU, memory, and disk features for training
features = ['cpu_usage', 'memory_usage', 'disk_usage']
X = df[features]

# Initialize and train the Isolation Forest model
# Isolation Forest is effective for anomaly detection in high-dimensional data
# It isolates anomalies by randomly selecting a feature and split value
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Save the trained model to disk
joblib.dump(model, 'isolation_forest.pkl')
