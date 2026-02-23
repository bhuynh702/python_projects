"""

File: cannon_ball.py
Author: Brittany Huynh
Date: 09/14/2023
E-mail: bhuynh4@umbc.edu
Description:

"""
import math

v0 = float(input('Enter the intial velocity: '))
angle = float(input('Enter the angle in degrees that you will fire the cannon: '))

two_theta_pi = (angle * 2 * math.pi)
one_eighty = (two_theta_pi / 180)
sine = (math.sin(one_eighty))
v_squared = (v0 ** 2)
sine_v_square = (sine * v_squared)
final_dis = (sine_v_square / 9.8)

print('The distance the cannon ball will travel is', final_dis,'meters')
              
        
