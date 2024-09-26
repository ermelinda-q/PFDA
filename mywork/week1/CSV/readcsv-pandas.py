# Module: Programming for Data Analytics - ATU
# Lecturer: Andrew Beatty
# Reading in the CSV as a pandas table
# Author: Ermelinda Qejvani
#


FILENAME = "data.csv"
DATADIR = "datafiles/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)

print(df)