"""

File: day_of_week_2
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: 09/2023
Description: This file determines what day of the week it is in October.

"""

# Input the day of October 2023
day = int(input("What day of October 2023 is it? "))

# Make sure that range stays between 1 to 31
if day > 31:
    print(f'That day {day} is out of range, you must enter a number between 1 and 31')

# Define a list of days of the week
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Oct. 1 is a Sunday, meaning that value[0] of the list is Oct. 1
day_of_week_num = (day - 1) % 7 

# Create if statements for the days that have different suffix than "th"
if day == 1:
    print(f'October {day}st is a Sunday.')
elif day == 2:
    print(f'October {day}nd is a Monday.')
elif day == 3:
    print(f'October {day}rd is Tuesday.') 
elif day == 21:
    print(f'October {day}st is a Saturday.')
elif day == 31:
    print(f'October {day}st is a Tuesday.')    
elif day == 22:
    print(f'October {day}nd is a Sunday.')
elif day == 23:
    print(f'October {day}rd is a Monday.')
elif 1 < day < 31:
    print(f"October {day}th is a {days_of_week[day_of_week_num]}")
