import pandas as pd
from sklearn.datasets import fetch_california_housing

try:
    print("Fetching California housing dataset...")
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df.to_csv('data/raw_data.csv', index=False)
    print("California housing dataset saved to data/raw_data.csv")
except Exception as e:
    print(f"Failed to fetch dataset: {e}")
    exit(1)
