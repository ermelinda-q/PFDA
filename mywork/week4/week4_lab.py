# Regular expressions - PFDA
# Purpose of this lab is to practice regular expressions in python.
# Based on week 4 lab by Andrew Beatty.
# Author: E. Qejvani

import re

regex = "\[.*\]"
filename = "smaller_access.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
        # if I did not want the [] at the beginning and end
        print(foundText[1:-1])
        
# Find all the ip addresses.
new_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(new_regex, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
        # if I did not want the [] at the beginning and end
        print(foundText[1:-1])