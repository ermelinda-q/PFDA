# Read in a simple file
# PFDA - Topic 1 - getting started
# Author: Ermelinda Qejvani
# Based on lectures from the above lecture

FILENAME = "data.txt"
DATADIR = "datafiles/"

print (DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line)
        print (f"{line} is size {len(line)}")
    print("")
    print(f"Total is {total}")