"""

File: ab_equality.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is a fun generator which gives you strings with equal amounts
of a's and b's depending on the given even number.

"""


def a_and_b(n, k, current):
    # n is the amount of times that the function will traverse until -
    # - n == 0, and k == 0, which means there's an equal number of a's and b's
    # k is what keeps track of the difference between the amount of a's and b's
    if n == 0 and k == 0:
        print(current)
        return  # if n == 0 and k == 0, the function returns the string
    elif n == 0:
        # once the number of iterations reaches 0, the function returns back to the previous iteration
        return
    else:
        # this the recursive call which adds a's and b's to the strings until the base cases are satisfied
        a_and_b(n - 1, k + 1, current + 'a')
        a_and_b(n - 1, k - 1, current + 'b')


if __name__ == '__main__':
    num = int(input("What length do you want to run? "))
    # will only run if the given num is even
    if num % 2 == 0:
        a_and_b(num, 0, '')
