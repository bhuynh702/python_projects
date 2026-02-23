"""

File: day_of_week.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Description: This file tells you what day of the week it is (in October 2023) depending on what number you put in.

"""

day = int(input('What day of October 2023 is it? '))

if day > 31:
    print(f'That day {day} is out of range, you must enter a number between 1 and 31')

if day == 1:
    print(f'October {day}st is a Sunday.')
elif day == 22:
    print(f'October {day}nd is a Sunday.')
elif day % 7 == 1 and day != 22 and 0 < day < 32: 
    print(f'October {day}th is a Sunday.')
    
if day == 2:
    print(f'October {day}nd is a Monday.')
elif day == 23:
    print(f'October {day}rd is a Monday.')
elif day % 7 == 2 and day != 23 and 0 < day < 32:
    print(f'October {day}th is a Monday.')
    
if day == 3:
    print(f'October {day}rd is Tuesday.')
elif day == 31:
    print(f'October {day}st is a Tuesday.')
elif day % 7 == 3 and day != 31 and 0 < day < 32:
    print(f'October {day}th is a Tuesday.')

if day == 4:
    print(f'October {day}th is Wednesday.')
elif day % 7 == 4 and 0 < day < 32:
    print(f'October {day}th is a Wednesday.')
    
if day == 5:
    print(f'October {day}th is Thursday.')
elif day % 7 == 5 and 0 < day < 32:
    print(f'October {day}th is a Thursday.')

if day == 6:
    print(f'October {day}th is Friday.')
elif day % 7 == 6 and 0 < day < 32:
    print(f'October {day}th is a Friday.')

if day == 7 or day == 14 or day == 28:
    print(f'October {day}th is Saturday.')
elif day == 21:
    print(f'October {day}st is a Saturday.')
