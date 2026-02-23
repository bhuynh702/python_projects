"""

File: distance.py
Author: Brittany Huynh
Date: 09/14/2023
E-mail: bhuynh4@gl.umbc.edu
Description: This file is a distance calculator. Simply put in your x and y coordinates and it will calculate the distance between the two points.

"""

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

x1_minus_x2 = (x1 - x2)
x1_x2_squared = (x1_minus_x2 ** 2)
y2_minus_y1 = (y2 - y1)
y2_y1_squared = (y2_minus_y1 ** 2)
add_points = (x1_x2_squared + y2_y1_squared)
distance_form = (add_points ** (1/2))

print('The distance between (',x1,',',y1,')', 'and', '(',x2,',',y2,')', 'is',distance_form)
