import joblib
import numpy as np

# Load the trained Isolation Forest model once at module level
MODEL_PATH = "isolation_forest_model.pkl"
model = joblib.load(MODEL_PATH)

def detect_anomaly(metrics):
    """
    Detect anomalies using a pre-trained Isolation Forest model.

    Parameters
    ----------
    metrics : list or np.ndarray
        Input metrics (1-D array-like) to be evaluated.

    Returns
    -------
    tuple
        (is_anomaly, anomaly_score)
        is_anomaly : bool
            True if the input is flagged as an anomaly, False otherwise.
        anomaly_score : float
            The anomaly score; lower values indicate stronger anomaly signal.
    """
    # Ensure input is a 2-D numpy array with shape (1, n_features)
    X = np.asarray(metrics).reshape(1, -1)

    # Predict: -1 for anomaly, 1 for normal
    pred = model.predict(X)[0]
    is_anomaly = pred == -1

    # Obtain anomaly score (negative values are anomalies)
    anomaly_score = model.score_samples(X)[0]

    return is_anomaly, anomaly_score
