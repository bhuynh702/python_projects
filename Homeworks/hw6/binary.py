"""

File: binary.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is a binary number calculator.

"""


def binary(number):
    # the base case is 1 since if the given number is 1, the binary of 1 is 1
    if number == 1:
        return str(1)
    # binary of 0 is 0
    elif number == 0:
        return str(0)
    else:
        # this is the recursive call which calculates the binary
        return binary(number // 2) + str(number % 2)


# the given starter code:
if __name__ == '__main__':
    x = int(input('Tell me number: '))
    while x != -1:
        print('0b' + binary(x), bin(x))
        x = int(input('Tell me number: '))
