# Week 5 Assignment - PFDA
# Author: E. Qejvani

# This program simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.

####################################################################
#################### Rules of Risk #################################
####################################################################

# In Risk one army fights another. (using 6 sided dice)
# In each battle round, the attacker can put forward up to three of their troops (3 dice).
# The defender can use up to two of their defending troops (2 dice).
# Each side looses troops depending on the following rules:
# The two top dice dice are compared (ie the attackers top dice roll with the defenders top dice roll) 
# If the attackers dice is the same or lower they loose one troop otherwise the defender looses a troop (ie if the attackers dice is higher)
# The next two highest dice from each side are then compared (ie the attackers second highest to the defenders second highest)
# If the attackers dice is the same or lower they loose one troop otherwise the defender looses a troop (ie if the attackers dice is higher)

# Importing modules needed for the game.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating an array of random numbers for both players using numpy (np).

# Attacker's array: Create, sort, and flip values in descending order.
attacker_roll = np.random.randint(1,7, size=(1000,3))
print("This is the attacker's roll\n")
print(attacker_roll)
attacker_roll.sort()
print("This is the attacker's roll sorted.\n")
print(attacker_roll)
attacker_roll_sorted = np.fliplr(attacker_roll)
attacker_roll_sorted = attacker_roll_sorted[:,:2]
print("This is the attacker's roll sorted.\n")
print(attacker_roll_sorted)

# Defender's array: Create, sort and flip values in descending order.
defender_roll = np.random.randint(1,7, size=(1000,2))
print("This is the defender's roll\n")
print(defender_roll)
defender_roll.sort()
print("This is the defender's roll\n")
print(defender_roll)
defender_roll_sorted = np.fliplr(defender_roll)
print("This is the defender's roll sorted.\n")
print(defender_roll_sorted)



# REFERENCES:
# https://discuss.codecademy.com/t/can-we-sort-numpy-arrays-in-reverse-order/357941
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order