import pandas as pd
import os

from utilities.yaml_loader import load_yaml_config

def stg_censo_2024__codigos_regiones():
    """
    Loads hogares data using the path defined in the YAML configuration.
    """
    # Load the YAML file as a dictionary
    config = load_yaml_config('models/staging/censo_2024/_src_censo_2024__codigos.yml')
    
    # Extract the path for the 'hogares' table
    tables = config['sources']['censos']['tables']
    rel_path = next(t['path'] for t in tables if t['name'] == 'region')
    
    # Construct the absolute path (project root is 3 levels up from this staging file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    file_path = os.path.join(project_root, rel_path)

    # read parquet
    df = pd.read_parquet(file_path)
    
    return df

def stg_censo_2024__codigos_provincias():
    """
    Loads hogares data using the path defined in the YAML configuration.
    """
    # Load the YAML file as a dictionary
    config = load_yaml_config('models/staging/censo_2024/_src_censo_2024__codigos.yml')
    
    # Extract the path for the 'hogares' table
    tables = config['sources']['censos']['tables']
    rel_path = next(t['path'] for t in tables if t['name'] == 'provincia')
    
    # Construct the absolute path (project root is 3 levels up from this staging file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    file_path = os.path.join(project_root, rel_path)

    # read parquet
    df = pd.read_parquet(file_path)
    
    return df

def stg_censo_2024__codigos_comunas():
    """
    Loads hogares data using the path defined in the YAML configuration.
    """
    # Load the YAML file as a dictionary
    config = load_yaml_config('models/staging/censo_2024/_src_censo_2024__codigos.yml')
    
    # Extract the path for the 'hogares' table
    tables = config['sources']['censos']['tables']
    rel_path = next(t['path'] for t in tables if t['name'] == 'comuna')
    
    # Construct the absolute path (project root is 3 levels up from this staging file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    file_path = os.path.join(project_root, rel_path)

    # read parquet
    df = pd.read_parquet(file_path)
    
    return df

