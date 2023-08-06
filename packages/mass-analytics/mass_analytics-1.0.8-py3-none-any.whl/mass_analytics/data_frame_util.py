import pandas as pd
import numpy as np
import datetime
from date import (get_periodicity, 
                  get_date_columns,
                  is_date)
from reader import read_data
import os

def pivot_by_key(df, index_column_names, key_column_names, values_column_names, agg_funcs='sum'):
    """
    Pivots a DataFrame based on the given keys and performs aggregation on the specified value columns.

    Parameters:
        df (pd.DataFrame): The DataFrame to pivot and perform aggregation on.
        index_column_names (list): List of column names to be used as index during pivoting.
        key_column_names (list): List of column names to be used as keys for pivoting.
        values_column_names (list): List of column names to be used as values for pivoting.
        agg_funcs (dict, optional): Dictionary mapping columns to aggregation functions. The default is {'column_name': 'sum'}.

    Returns:
        pd.DataFrame: The resulting pivoted DataFrame with aggregation.
    """
    
    df['key'] = df.apply(lambda x: '_'.join([str(x[st]) for st in key_column_names]), axis=1)
    pivot_table = pd.pivot_table(df, values=values_column_names, index=index_column_names, columns='key', aggfunc=agg_funcs, fill_value=0)

    new_df = pd.DataFrame()
    for cols in pivot_table.columns:
       new_df['_'.join(cols)] = pivot_table[cols]
       
    new_df.reset_index(inplace=True)
    
    return new_df

def get_mapping_table(df, date_column_name, column_values, freq=None):
    """
    Create a mapping table based on the provided DataFrame, date column, and column values.

    The function generates a new DataFrame that contains all unique combinations of the date
    values (within the specified frequency) and the unique values of each column in the 
    'column_values' list.

    Parameters:
        df (pandas.DataFrame): The original DataFrame containing the data.
        date_column_name (str): The name of the column that holds the date values.
        column_values (list): A list of column names for which unique values will be used
                              to create combinations in the mapping table.
        freq (str, optional): The frequency string for date_range(). 
                              Defaults to None, in which case the function will attempt 
                              to infer the frequency from the DataFrame using get_periodicity().

    Returns:
        pandas.DataFrame: A new DataFrame representing the mapping table with date_column_name 
                          and unique values from each column in column_values.

    Note:
        - If the 'freq' parameter is not provided, the function will attempt to infer it from the 
          date_column_name using the get_periodicity() function.
        - Make sure to provide a valid 'freq' frequency string, such as 'D' for daily, 'M' for monthly, 
          'Y' for yearly, etc.
        - The returned DataFrame will have a row for each unique combination of date and column 
          values from the original DataFrame.
    
    """

    # Get freq
    if freq == None:
        freq = get_periodicity(df, date_column_name)[date_column_name]
    if freq == None:
        freq = 'D'
    
    new_df = pd.DataFrame()
    
    new_df[date_column_name] = pd.date_range(start=min(df[date_column_name]), end=max(df[date_column_name]), freq=freq, inclusive='both')

    for col in column_values:
        new_df = new_df.join(pd.DataFrame(df[col].unique()), how='cross')
        new_df.rename(columns={0: col}, inplace=True)
    
    return new_df

def map_table(df, mapping_table):
    """
    Map data from the original DataFrame to the provided mapping table.

    The function performs a left merge between the mapping_table and the original DataFrame (df) 
    based on their common columns. It fills in missing values in the merged DataFrame with 0.

    Parameters:
        df (pandas.DataFrame): The original DataFrame containing the data to be mapped.
        mapping_table (pandas.DataFrame): The mapping table containing unique combinations of 
                                          data and columns to which the original data will be 
                                          mapped.

    Returns:
        pandas.DataFrame: A new DataFrame resulting from the left merge of the mapping_table and 
                          the original DataFrame (df), with missing values filled in with 0.
    
    Note:
        - The merge is performed based on the common columns between the mapping_table and the 
          original DataFrame. Make sure that the mapping_table and the df have at least one 
          common column.
        - Any missing values in the merged DataFrame are filled with 0.
        - The returned DataFrame will have the same number of rows as the mapping_table and will 
          include the additional columns from the original DataFrame (df) that matched the 
          common columns in the mapping_table.
    
    """

    return mapping_table.merge(df, how='left').fillna(0)

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def data_summary(*args):
    """
    Print a summary of data for each given file.

    Parameters:
        *args (str): Paths to CSV, XLSX, or XLS files.

    Prints:
        - File name
        - Date column (if present)
        - Periodicity (if date column is detected)
        - Start date (if date column is detected)
        - End date (if date column is detected)
    """

    for path in args:
        df = read_data(path)
        file_name = os.path.basename(path).split('/')[-1]
        try:
            columns = get_date_columns(df)
        except:
            print(f"{Color.YELLOW}", "No date columns found in", file_name, f"{Color.RESET}")
            print()
            continue
        
        if type(columns) is str:
            columns = [columns]
            
        print(f"{Color.GREEN}", file_name, f"{Color.RESET}")
        periodicity = get_periodicity(df)

        for col in columns:
            col_serie = df[col]
            if np.issubdtype(df[col].dtype, np.object_):
                col_serie = col_serie[col_serie.apply(lambda x: isinstance(x, datetime.datetime) or is_date(x))]
                col_serie = col_serie.astype('datetime64[ns]')

            if col == columns[-1]:
                sep = f'{Color.GREEN}    └── {Color.RESET}'
            else:
                sep = f'{Color.GREEN}    ├── {Color.RESET}'
            print(sep,
                  f"{Color.CYAN}Date column:{Color.RESET}",
                  col,
                  f"{Color.CYAN}Periodicity:{Color.RESET}",
                  periodicity[col],
                  f"{Color.CYAN}Start Date:{Color.RESET}",
                  min(col_serie)._date_repr,
                  f"{Color.CYAN}End Date:{Color.RESET}",
                  max(col_serie)._date_repr)
            
        print()
            



