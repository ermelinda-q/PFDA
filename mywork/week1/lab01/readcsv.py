# Programming for Data Analytics
# Week 1 - Data representation.
# Lab 01 - read .csv file
# Author: Ermelinda Qejvani

# This program reads in the data from a .csv file and output each line as a list.

import csv

FILENAME = "data.csv"
DATADIR = "datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)# quote parameter to read in numbers as floats.
    linecount = 0
    total = 0   # will hold total of all ages in files
    for line in reader:
        if not linecount: # first row is header row
            pass
        else:   # all subsequent rows
            total += int(line[1])   # line 1 holds the age value, 0 holds 'id'
        linecount += 1
    print(f"Average age is {total/(linecount-1)}")  # -1: removing first row-header data.
    


# READ IN CSV FILE AS A DICTIONARY OBJECT#
##########################################

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print(line)
        count += 1
    print(f"Average is {total/(count)}") # no need for '-1' DictReader adds the data to the appropriate headings?
    