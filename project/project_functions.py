###########################################
### PFDA - BIG PROJECT - functions file ###
###########################################

# Author: E. Qejvani

import pandas as pd

################## Function 1 ########################

# This function counts the rows with empty cells or a single space as a value.
def count_rows_with_empty_or_space_cells_detail(df):  
    # Create a Boolean DataFrame where cells equal ' ' or NaN are True
    df_boolean = (df == ' ') | (df.isnull())  # Checks for both empty space ' ' and NaN values

    # Count the number of missing values (spaces or NaN) in each row
    row_counts = df_boolean.sum(axis=1)

    # Create a dictionary to store how many rows have missing cells
    missing_counts = row_counts.value_counts().sort_index()
    # Variable to hold the rows with at least one empty cell
    total_rows_with_no_value = 0
    # Print the detailed count of rows with empty cells and add the total
    for count, rows in missing_counts.items():
        print(f"Rows with {count} empty cells: {rows}")
        if count > 0:  # Only add rows with at least one empty cell
            total_rows_with_no_value += rows
    
    print(f"Total rows with at least one empty values: {total_rows_with_no_value}")

    # Return the total rows with all values
    return total_rows_with_no_value


################### Function 2 ##########################

# This function cleans/removes all the rows that contain missing data in the DataFrame.
# def remove_rows_with_missing_data(df):  
#     # Create a Boolean DataFrame where cells equal ' ' or NaN are True
#     df_to_clean = (df == ' ') | (df.isnull())  # Checks for both empty space ' ' and NaN values
#     
#     # Remove rows with any missing data (either ' ' or NaN)
#     df_cleaned = df[~df_to_clean.any(axis=1)]  # Keep rows where no cells are missing
#     
#     return df_cleaned
def remove_rows_with_missing_data(df):
   
    # Replace empty strings and single spaces with NaN for consistent handling
    df = df.replace(['', ' '], pd.NA)
    
    # Drop rows where any value is NaN
    df_cleaned = df.dropna()
    
    return df_cleaned


##################### Function 3 ########################

# This function converts the data type of a column/columns to numeric data.
def convert_columns_to_float(df, columns):
   
    # loop to convert more than one set/column of data to numeric.
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
