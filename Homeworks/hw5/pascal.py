"""
File: pascal.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: October 2023
Description: This file is a pascal's triangle calculator.

"""
# this function next_level is what adds the input
# together and puts '1' back at the end of the list
def next_level(level):
    pascal = [1] # the first column in the triangle will be all 1's
    for x in range(len(level) - 1): # for every number for the length of the input - 1
                                    # e.g. input = 1 2 3 , length is 3-1
        pascal.append(level[x]+(level[x + 1])) # the for loop iters (adds numbers 1+2, 2+3)
                                                # through only 2 times
    pascal.append(1)
    return pascal

if __name__ in '__main__':
    level = [1]
    for i in range(10):
        for x in level:
            print(x, end='\t')
        print()
        level = next_level(level)
    in_string = input('What values do you want to run next_level on? ')
    while in_string != '':
        values = []
        for x in in_string.split():
            values.append(int(x))
        print(next_level(values))
        in_string = input('What values do you want to run next_level on? ')
