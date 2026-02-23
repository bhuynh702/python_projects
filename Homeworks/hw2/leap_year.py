"""

File: leap_year.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Description: This file tells you if a year you input in a leap year or not.

"""

year_choice = int(input('Enter a year: '))

if (year_choice % 4 == 0 and year_choice % 100 != 0) or (year_choice % 400 == 0):
    print(year_choice,'is a leap year.')
else:
    print(year_choice,'is not a leap year.')
