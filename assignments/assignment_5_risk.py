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
import numpy as np
import matplotlib.pyplot as plt


# Defining a function to create arrays using numpy.
# The function creates, sorts, and re-sorts the arrays in descending order.
# It also truncates the array to the highest two values, if necessary(attacker's draws).
def roll_dice(number_of_dice):
    rolls = np.random.randint(1, 7, size=(1000,number_of_dice))
    rolls.sort(axis=1)
    rolls_sorted = np.fliplr(rolls)
    return rolls_sorted[:, :2]          # Reads the first (highest) two values of the player.

attacker_rolls = roll_dice(3)       # call function for the attacker.
defender_rolls = roll_dice(2)       # call function for the defender.

# print(attacker_rolls)               # checking that the function works.
# print(defender_rolls)               # it works!!!


# Setting up number of battles to 1000.
number_of_battles = 1000     

# Initializing counters for battle wins and draws.       
attacker_battle_wins = 0
defender_battle_wins = 0
total_draws = 0

# Comparing the two rolls for each player.
for i in range(number_of_battles):
    
    # Setting number of wins to zero before the battle.
    attacker_wins = 0   
    defender_wins = 0
    draws = 0 
    
    # Compare the two attacker rolls against the two defender rolls
    for a_roll, d_roll in zip(attacker_rolls[i], defender_rolls[i]):
        if a_roll > d_roll:
            attacker_wins += 1  # Increment attacker wins for this comparison
        elif a_roll < d_roll:
            defender_wins += 1  # Increment defender wins for this comparison
        else:
            draws += 1  # Increment draws for this comparison

    # After comparing both rolls, deciding who wins the battle.
    if attacker_wins > defender_wins:
        attacker_battle_wins += 1  # Attacker wins the battle
    elif defender_wins > attacker_wins:
        defender_battle_wins += 1  # Defender wins the battle
    else:
        total_draws += 1  # If both have the same number of wins, it's a draw

# Print out final results.
print(f"Total results after {number_of_battles} battles:")
print(f"Attacker battle wins: {attacker_battle_wins}, Defender battle wins: {defender_battle_wins}, Total draws: {total_draws}")



# REFERENCES:
# https://discuss.codecademy.com/t/can-we-sort-numpy-arrays-in-reverse-order/357941
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
# https://discuss.python.org/t/separate-for-loops-in-zip-objects-with-different-loop-variables/52961/2