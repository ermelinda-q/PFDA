# PFDA - Lab on Pandas 
# Week 3 - Revision on Pandas
# Author: E. Qejvani

import pandas as pd

# Create dataset using lists(list with list).
listDAta= [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]
# Set the column names.
df = pd.DataFrame(listDAta, columns=['name','subject','grade']) 
print(df.head(3))                   # print the first three records.

# Use the describe function to see the overall stats on the grades. 
print(df.describe())

# Use the type function to see that this output is a dataframe.
print(type(df.describe()))

# Write this dataframe to a csv file called grades.csv.
path = "../data/"
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

# Write it to an excel file called grades.xlsx (in sheet ‘data’)
# without the index column.
excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

# Add the description to another sheet called ‘summary’. We will need to change
# the writer to open from the default writer. (if we get a permission denied, close
# the workbook in excel).
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")

# Calculate and print the mean of the grades.
mean = df.describe().loc['mean','grade']
print(mean)
# or
mean = df['grade'].mean()
print (mean)