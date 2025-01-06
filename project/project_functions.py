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
def remove_rows_with_missing_data(df):
   
    # Replace empty strings and single spaces with NaN for consistent handling
    df = df.replace(['', ' '], pd.NA)
    
    # Drop rows where any value is NaN
    df_cleaned = df.dropna()
    
    return df_cleaned


##################### Function 3 ########################

# This function converts the data type of a column/columns to numeric data.
# I'm converting the data type to float32 to use less memory because of the large amount of data in my dataset.
def convert_columns_to_float(df, columns):
   
    # loop to convert more than one set/column of data to numeric.
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce').astype('float32') 
    return df


#################### Function 4 #########################

# This function calculate air density(kg/m³) from data available in the dataset: temperature, vapor pressure and mean sea level pressure.
def calculate_air_density(temp, vappr, msl):
    
    # Constants needed for our formula
    R_dry = 287.05  # Specific gas constant for dry air in J/(kg·K)
    R_vapor = 461.5  # Specific gas constant for water vapor in J/(kg·K)
    
    # Convert temperature to Kelvin
    T = temp + 273.15
    
    # Convert vapor pressure and mean sea level pressure from hectoPascals(hPa) to Pascals(Pa)
    P_vapor = vappr * 100  # Vapour pressure in Pa
    P_msl = msl * 100  # Mean sea level pressure in Pa
    
    # Calculate the partial pressure of dry air
    P_dry = P_msl - P_vapor  # Dry air pressure in Pa
    
    # Calculate air density using the formula
    air_density = (P_dry / (R_dry * T)) + (P_vapor / (R_vapor * T))
    
    return air_density


#################### Function 5 ###########################

# This function adds a new column(air_density) to our dataset. It calls the calucalte_air_density function.
# After the air density calculations removes the columns used.
def add_air_density_column(df):
    
    # Apply the air density calculation function row-wise
    df['air_density'] = df.apply(lambda row: calculate_air_density(row['temp'], row['vappr'], row['msl']), axis=1)
    
    # Remove the columns that are no longer needed
    df = df.drop(columns=['temp', 'vappr', 'msl'])  # Remove these columns
    
    return df


##################### Function 6 ############################

# This function groups a given dataset by the time entered as a parameter.
def group_by_dataset(df, time='D'):
    if time == 'decade':
        # Create a temporary DataFrame with the 'decade' column
        df_temp = df.copy()  # Avoid modifying the original DataFrame
        df_temp['decade'] = (df_temp.index.year // 10) * 10
        # Group by decade.
        grouped_df = df_temp.groupby('decade').size()
    else:
        # For daily, weekly, monthly, or yearly grouping
        grouped_df = df.resample(time).size()
    
    return grouped_df
