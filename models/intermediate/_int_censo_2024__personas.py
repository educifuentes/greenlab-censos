import pandas as pd

from models.staging.censo_2024._stg_censo_2024__personas import stg_censo_2024__personas

def int_censo_2024__personas():
    df = stg_censo_2024__personas()

    # replace survey codes with categorical values

    return df
