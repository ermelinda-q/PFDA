# Read in a csv file.
# PFDA - Topic 1 - getting started
# Author: Ermelinda Qejvani
# Based on lectures from Andrew Beatty

import csv

FILENAME = "data.csv"
DATADIR = "datafiles/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # or: if linecount == 0
            print(f"{line}\n------------------------")
        else:       # all other raws
            total += int(line[0])
            print(line)
        linecount += 1
