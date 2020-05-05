import pandas as pd
import numpy as np

def remove_empty_rows(dataframe: pd.DataFrame, column_name: str):
    """
    Any rows where there is " " or "" in the [column_name] column will be removed.
    There will be a print statement displaying how many rows were dropped.

    Parameters
    ----------
    dataframe : pd.DataFrame
        dataframe to be changed.
        
    column_name: str
        name of the column that will be analyzed. This will determine what rows will be deleted

    Returns
    -------
    None.

    """
    original_size = len(dataframe)
    dataframe[column_name].replace(" ", np.nan, inplace=True)
    dataframe[column_name].replace("", np.nan, inplace=True)
    dataframe.dropna(subset=[column_name], inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    new_size = len(dataframe)
    print(f"A total of {original_size - new_size} rows were dropped")


def get_dataframe_sample(dataframe: pd.DataFrame, fraction: float) -> pd.DataFrame:
    """
    Get a random sample of the a dataframe.
    Parameters
    ----------
    dataframe : pd.DataFrame
        dataframe that the sample will be made from.
    fraction : float
        The fraction of the dataframe you wish to have.

    Returns
    -------
    TYPE
        returns a new dataframe based on the fraction chosen Original index
        is removed for convenience.

    """
    df = dataframe.sample(frac = fraction)
    return df.reset_index(drop=True)

