import pandas as pd

from models.staging.censo_2024._stg_censo_2024__personas import stg_censo_2024__personas

from utilities.data_transformations.survey_processing import map_survey_codes

def int_censo_2024__personas():
    df = stg_censo_2024__personas()

    # replace survey codes with categorical values
    mapping_path = 'models/staging/censo_2024/docs/personas_censo_mapping.json'
    df = map_survey_codes(df, mapping_path)

    return df
