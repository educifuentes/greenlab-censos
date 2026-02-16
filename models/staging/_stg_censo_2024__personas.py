import pandas as pd
import os
from utilities.yaml_loader import load_yaml_config

def get_stg_censo_2024__personas():
    """
    Loads personas data using the path defined in the YAML configuration.
    """
    # Load the YAML file as a dictionary
    config = load_yaml_config('models/staging/_src_censos.yml')
    
    # Extract the path for the 'personas' table
    tables = config['sources']['censos']['tables']
    csv_rel_path = next(t['path'] for t in tables if t['name'] == 'personas')
    
    # Construct the absolute path (project root is 2 levels up from this staging file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    csv_path = os.path.join(project_root, csv_rel_path)

    df = pd.read_csv(csv_path, delimiter=';')
    
    # Read and return the dataframe
    return df
