import kfp
from kfp import dsl
from kfp.components import create_component_from_func, InputPath, OutputPath

def data_extraction(data_url: str, output_csv: OutputPath(str)):
    """
    Downloads the dataset from a source (simulating DVC get/import or direct download).
    For this assignment, we'll fetch the California housing dataset directly 
    to ensure it works in the isolated container environment.
    """
    import pandas as pd
    from sklearn.datasets import fetch_california_housing
    
    print(f"Fetching data from {data_url}...")
    # In a real DVC scenario, we would use:
    # import dvc.api
    # with dvc.api.open(data_url) as f:
    #     df = pd.read_csv(f)
    
    # For simplicity and robustness in this demo:
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    df.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")

def data_preprocessing(input_csv: InputPath(str), 
                       train_csv: OutputPath(str), 
                       test_csv: OutputPath(str)):
    """
    Loads data, cleans it, and splits into train/test sets.
    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    
    print("Loading data...")
    df = pd.read_csv(input_csv)
    
    # Simple preprocessing: Drop rows with missing values (if any)
    df.dropna(inplace=True)
    
    print("Splitting data...")
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    train_df.to_csv(train_csv, index=False)
    test_df.to_csv(test_csv, index=False)
    print("Data split and saved.")

def model_training(train_csv: InputPath(str), 
                   model_pkl: OutputPath(str)):
    """
    Trains a Random Forest classifier (regressor for housing data) and saves the model.
    """
    import pandas as pd
    import joblib
    from sklearn.ensemble import RandomForestRegressor
    
    print("Loading training data...")
    df = pd.read_csv(train_csv)
    X = df.drop('target', axis=1)
    y = df['target']
    
    print("Training model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    print("Saving model...")
    joblib.dump(model, model_pkl)
    print(f"Model saved to {model_pkl}")

def model_evaluation(test_csv: InputPath(str), 
                     model_pkl: InputPath(str),
                     metrics_json: OutputPath(str)):
    """
    Evaluates the model and saves metrics.
    """
    import pandas as pd
    import joblib
    import json
    from sklearn.metrics import mean_squared_error, r2_score
    
    print("Loading test data and model...")
    df = pd.read_csv(test_csv)
    X_test = df.drop('target', axis=1)
    y_test = df['target']
    
    model = joblib.load(model_pkl)
    
    print("Predicting...")
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        'mse': mse,
        'r2': r2
    }
    
    print(f"Metrics: {metrics}")
    
    with open(metrics_json, 'w') as f:
        json.dump(metrics, f)
    print(f"Metrics saved to {metrics_json}")

if __name__ == '__main__':
    # Compile components
    create_component_from_func(
        data_extraction,
        output_component_file='components/data_extraction.yaml',
        base_image='python:3.8',
        packages_to_install=['pandas', 'scikit-learn']
    )
    
    create_component_from_func(
        data_preprocessing,
        output_component_file='components/data_preprocessing.yaml',
        base_image='python:3.8',
        packages_to_install=['pandas', 'scikit-learn']
    )
    
    create_component_from_func(
        model_training,
        output_component_file='components/model_training.yaml',
        base_image='python:3.8',
        packages_to_install=['pandas', 'scikit-learn', 'joblib']
    )
    
    create_component_from_func(
        model_evaluation,
        output_component_file='components/model_evaluation.yaml',
        base_image='python:3.8',
        packages_to_install=['pandas', 'scikit-learn', 'joblib']
    )
    print("Components compiled to YAML files in components/ directory.")
