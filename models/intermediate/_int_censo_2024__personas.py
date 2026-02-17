import pandas as pd

from models.staging.censo_2024._stg_censo_2024__personas import stg_censo_2024__personas
from models.staging.censo_2024._stg_censo_2024__codigos import stg_censo_2024__codigos_regiones, stg_censo_2024__codigos_provincias, stg_censo_2024__codigos_comunas

from utilities.data_transformations.survey_processing import map_survey_codes

def int_censo_2024__personas():
    personas_df = stg_censo_2024__personas()

    # replace survey codes with categorical values
    mapping_path = 'models/staging/censo_2024/docs/personas_censo_mapping.json'
    personas_df = map_survey_codes(personas_df, mapping_path)

    # join with geo code tables
    personas_df = pd.merge(personas_df, stg_censo_2024__codigos_regiones(), left_on='region', right_on='cod_region', how='left')
    personas_df = pd.merge(personas_df, stg_censo_2024__codigos_provincias(), left_on='provincia', right_on='cod_provincia', how='left')
    personas_df = pd.merge(personas_df, stg_censo_2024__codigos_comunas(), left_on='comuna', right_on='cod_comuna', how='left')

    # drop the original columns
    personas_df.drop(columns=['region', 'provincia', 'comuna'], inplace=True)

    # reorder columns
    leading_cols = ['id_persona', 'region_nombre', 'provincia_nombre', 'comuna_nombre']
    # Only include existing columns to be safe
    leading_cols = [c for c in leading_cols if c in personas_df.columns]
    other_cols = [c for c in personas_df.columns if c not in leading_cols]
    
    personas_df = personas_df[leading_cols + other_cols]

    return personas_df
