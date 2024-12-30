###########################################
### PFDA - BIG PROJECT - functions file ###
###########################################

# Author: E. Qejvani

import pandas as pd

# This function counts the rows with empty cells or a single space as a value.
def count_rows_with_empty_or_space_cells_detail(df):  
    # Create a Boolean DataFrame where cells equal ' ' or NaN are True
    df_boolean = (df == ' ') | (df.isnull())  # Checks for both empty space ' ' and NaN values
    
    # Count the number of missing values (spaces or NaN) in each row
    row_counts = df_boolean.sum(axis=1)
    
    # Create a dictionary to store how many rows have 1, 2, ..., n missing cells
    missing_counts = row_counts.value_counts().sort_index()

    # Print the detailed count of rows with empty cells
    for count, rows in missing_counts.items():
        print(f"Rows with {count} empty cells: {rows}")

    return missing_counts

# This function cleans/removes all the rows that contain missing data in the DataFrame.
def remove_rows_with_missing_data(df):  
    # Create a Boolean DataFrame where cells equal ' ' or NaN are True
    df_boolean = (df == ' ') | (df.isnull())  # Checks for both empty space ' ' and NaN values
    
    # Remove rows with any missing data (either ' ' or NaN)
    df_cleaned = df[~df_boolean.any(axis=1)]  # Keep rows where no cells are missing
    
    return df_cleaned


