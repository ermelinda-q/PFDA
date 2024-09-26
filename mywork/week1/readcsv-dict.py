# Read in a csv file as a dictionary
# PFDA - Topic 1 - getting started
# Author: Ermelinda Qejvani
# Based on lectures from Andrew Beatty

import csv

FILENAME = "data.csv"
DATADIR = "datafiles/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    for line in reader:
        total += int(line["id"])
        print(line)
        
