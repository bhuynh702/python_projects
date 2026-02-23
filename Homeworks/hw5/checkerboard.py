"""
File: checkerboard.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: October 2023
Description: This file creates a square based on two symbols the user inputs.

"""
# this function creates the size of the square and
# alternates the symbols of the square
def checkerboard(size, symbol_1, symbol_2):

    for x in range(size): # this is the horizontal size
        for y in range(size): # this is the vertical size
            if (x + y) % 2 == 0: # if the L + W is even
                print(symbol_1, end='') # it will print the symbol_1
            else:
                print(symbol_2, end='') # if it's not even it will alternate
                                        # the pattern
        print()


if __name__ == '__main__':
    size = int(input("What size do you want? "))
    symbols = input("What symbols do you want? ")
    symbol_1 = symbols[0] # we set symbol_1 to the first index of the string
    symbol_2 = symbols[2] # we set symbol_2 to the 2nd index of the string
    # we call the function with the input as the parameters
    checkerboard(size, symbol_1, symbol_2)
