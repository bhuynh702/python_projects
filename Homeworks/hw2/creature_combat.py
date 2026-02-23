"""

File: creature_combat.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Description: This is simple game where creatures fight each other.

"""

name_1 = input('What is the name of the first creature? ')
power_1 = int(input('What is the power of the first creature? '))
tough_1 = int(input('What is the toughness of the first creature? '))

name_2 = input('What is the name of the second creature? ')
power_2 = int(input('What is the power of the second creature? '))
tough_2 = int(input('What is the toughness of the second creature? '))

result_1 = (tough_1 - power_2)

print("The first creature now has (",power_1,",",result_1,")")

result_2 = (tough_2 - power_1)

print("The second creature now has (",power_2,",",result_2,")")

if result_1 < 0 and result_2 > 0:
    print(name_1,'has died,',name_2,'wins')
elif result_1 < 0 and result_2 < 0:
    print('Both creatures died in mutual combat')
elif result_1 > 0 and result_2 > 0: 
    print('Both creatures live to fight another day')
