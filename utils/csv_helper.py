import pandas as pd

def save_to_csv(data, filename, columns):
    """Save a list of data to a CSV file."""
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(filename, index=False)

def read_csv(filename):
    """Read a CSV file and return its data as a DataFrame."""
    return pd.read_csv(filename)
