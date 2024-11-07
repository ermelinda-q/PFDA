# PFDA - Task 4
# Author: E. Qejvani

# Task: Write a function (named `number_days_between`) that:

# 1 - Takes two arguments that are 8-digit integers of the form YYYYMMDD (actually a date), and
# 2 - Returns the number of days between the two dates.

from datetime import datetime

def number_days_between():
    # Adding a while loop to check for user input until user enters correct day format.
    while True:
        try:
            # creating variables date_one and date_two to hold values entered by user input in an integer format.
            date_one = int(input("Enter the first date (YYYYMMDD): "))
            date_two = int(input("Enter the second date (YYYYMMDD): "))

            # Convert the integers to strings and then to datetime objects
            date_one_str = str(date_one)
            date_two_str = str(date_two)
            date_format = "%Y%m%d"
            
            date_one_obj = datetime.strptime(date_one_str, date_format)
            date_two_obj = datetime.strptime(date_two_str, date_format)
            
            # Calculate the difference in days using abs value.
            difference = abs((date_two_obj - date_one_obj).days)
            return difference
        except ValueError:
            print("Invalid date format. Please enter the date in YYYYMMDD format.")

# Loop until the user types correctly "yes" or "no".
while True:
    user_choice = input("Do you want to calculate the number of days between two dates? (yes/no): ").strip().lower()
    if user_choice in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# If the user says yes, function is called, if not message displayed.
if user_choice == "yes":
    days_between = number_days_between()
    print(f"The number of days between the two dates is: {days_between}")
else:
    print("Goodbye!")
