from typing import Any

import pandas as pd
from config import CSV_PATH


# reading the csv data
df = pd.read_csv(CSV_PATH)
# setting None for the null data
df = df.where(pd.notnull(df), None)
#converting the given list data into dictionary
data = df.to_dict(orient="records")

# to get all the csv data
def get_csv_data() -> list[dict]:
    """
    Reads a CSV file and returns its content as a list of dicts.
    Converts NaN to None for JSON compatibility.
    """
    try:
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at {CSV_PATH}")
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty or corrupt")
    except Exception as e:
        raise e

# to get the specific data by name
def get_single_data_without_category(name:str) -> dict | None:
    try:
        for i in range(len(data)):
            if data[i]["name"].casefold() == name.casefold():
                return data[i]
    except Exception as e:
        raise e

# to get the data according to the category "region"
def get_single_data_with_category(region:str) -> list[dict]:
    try:
        result = []
        for i in range(len(data)):
            if data[i]["region"] is not None and data[i]["region"].casefold() == region.casefold():
                result.append(data[i])
        return result
    except Exception as e:
        raise e





