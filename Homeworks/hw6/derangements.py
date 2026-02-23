"""

File: derangements.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is a calculator for a recursive
formula to calculate derangements.

"""


def derangement(num):
    # the base case is num = 0, since D(0) = 1 so returns 1
    if num == 0:
        return 1
    else:
        # this is the coded version of the given formula
        return num * derangement(num - 1) + (-1) ** num


# the given starter code:
if __name__ == '__main__':
    test_num = int(input('What Dn do you want to compute? '))
    while test_num != -1:
        print(test_num, derangement(test_num))
        test_num = int(input('What Dn do you want to compute? '))
