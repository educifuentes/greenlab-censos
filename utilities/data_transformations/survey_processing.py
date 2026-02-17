import pandas as pd
import json
import os

def map_survey_codes(df: pd.DataFrame, mapping_path: str) -> pd.DataFrame:
    """
    Maps survey codes in a dataframe to their corresponding text values based on a JSON mapping file.
    Converts mapped columns to categorical dtype.

    Args:
        df (pd.DataFrame): The dataframe containing survey data.
        mapping_path (str): Path to the JSON file containing the mapping. 
                            Can be absolute or relative to the project root.

    Returns:
        pd.DataFrame: The dataframe with mapped values and categorical columns.
    """
    # Resolve mapping path relative to project root if it's not absolute
    if not os.path.isabs(mapping_path):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        mapping_path = os.path.join(project_root, mapping_path)

    if not os.path.exists(mapping_path):
        raise FileNotFoundError(f"Mapping file not found at: {mapping_path}")

    with open(mapping_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    # Copy df to avoid setting on copy warning if a slice was passed
    df = df.copy()

    for col, codes in mapping.items():
        if col in df.columns:
            # Ensure column is treated as object/string for mapping to work if keys in json are strings
            # But keys in JSON are always strings. If df has ints, we need to handle that.
            # Best practice: convert column to string temporarily for mapping, or convert keys to match col type?
            # Given typically survey codes are integers but can be 'NA', '99', etc, mixed types happen.
            # Safe bet: Convert series to string, map, then categorical.
            
            # Helper to handle potential mixed types in source or map keys
            # The mapping keys in the provided JSON are strings ("1", "2", ...)
            
            # Convert column to string to ensure matching with JSON keys
            df[col] = df[col].astype(str)
            
            # Map values
            # Using map alone might produce NaNs for unmapped values if we don't pass a fallback.
            # simpler approach: use replace. But replace might be slow on large DFs.
            # map is faster. Let's use map and fillna with original if needed, but here we want to map.
            # If a value is NOT in the map, it should probably stay as is or become NaN?
            # Usually we want to keep it if it's not a code, but typically all valid codes are mapped.
            
            # Let's use replace for safety on partial matches (though map is better for full col transformation)
            # Actually, let's look at the requirement: "map th evalues of the df to the adhoc values"
            
            df[col] = df[col].map(codes).fillna(df[col])
            
            # Convert to category
            df[col] = df[col].astype('category')

    return df
