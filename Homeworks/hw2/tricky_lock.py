"""

File: tricky_lock.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Description: This file is a tricky lock, enter the combination to see if it opens or not!

"""

num_1 = int(input('What is the first number in the combination lock? '))
num_2 = int(input('What is the second number in the combination lock? '))
pos_1 = input('What is the position of the first switch (up/down)? ')
pos_2 = input('What is the position of the second switch (up/down)? ')
pos_3 = input('What is the position of the third switch (up/down)? ')

lock_nums = num_1 + num_2
switch_positions = (pos_1, pos_2, pos_3)

good_combination = switch_positions in (('up', 'up', 'down'), ('down', 'up', 'up'), ('up', 'down', 'up'))

if lock_nums == 36 and good_combination:
    print('The lock opens.')
elif lock_nums != 36 and good_combination:
    print('The lock clanks but doesn\'t open.')
elif (lock_nums == 36) and (good_combination == False):
    print('The lock clanks but doesn\'t open.')
else:
    print('The lock doesn\'t open')
