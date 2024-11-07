# PFDA - Lecture 1 task 3
# Task: Create an arbitrary `date` object and add five weeks. Print the new date.
# Author: E. Qejvani

import datetime 

a_date = datetime.date(year=2022, month=11, day=1)

new_date = a_date + datetime.timedelta(weeks=5)
print(new_date)

# trying an exercise from the lecture:

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(f"{attr}: {getattr(d, attr)}")