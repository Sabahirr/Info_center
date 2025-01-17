import pandas as pd
import streamlit as st


# Cache edilmiş yükləmə funksiyası
@st.cache_data
def load_data(file_path: str):
    return pd.read_parquet(file_path, engine='pyarrow')


def filter_csv_by_column(df, column_name, filter_value):
    """
    Filters a DataFrame based on a specific column's value and returns the filtered data.

    Args:
        df (pd.DataFrame): DataFrame to filter.
        column_name (str): Column name to filter by.
        filter_value (str): Value to filter the column by.

    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    # Ensure the column and filter value are strings and strip extra spaces
    df[column_name] = df[column_name].astype(str).str.strip()
    filter_value = str(filter_value).strip()

    # Apply the filter
    filtered_data = df[df[column_name] == filter_value]

    return filtered_data
