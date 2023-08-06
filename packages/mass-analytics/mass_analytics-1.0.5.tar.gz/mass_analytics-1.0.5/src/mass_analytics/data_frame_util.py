import pandas as pd


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


