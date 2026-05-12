import pandas as pd
import os

def save_metrics(metrics, file_path):
    """
    Append metrics data into a CSV file.
    If the file does not exist, create it with a header row.
    
    Parameters:
        metrics (dict or list[dict]): Metrics to save. If dict, a single row;
                                      if list[dict], multiple rows.
        file_path (str): Path to the CSV file.
    
    The metrics are used to track AI training performance over time,
    enabling reproducibility and comparison across experiments.
    """
    # Normalize to list of dicts
    if isinstance(metrics, dict):
        metrics = [metrics]

    df_new = pd.DataFrame(metrics)

    # If file exists, append without header; otherwise write with header
    if os.path.isfile(file_path):
        df_new.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df_new.to_csv(file_path, mode='w', header=True, index=False)


def load_dataset(file_path):
    """
    Load a dataset from a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: The loaded dataset.
    
    This dataset is intended for training and evaluating AI models.
    Ensure the file contains properly formatted data suitable for machine learning tasks.
    """
    return pd.read_csv(file_path)
