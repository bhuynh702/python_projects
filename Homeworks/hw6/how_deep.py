"""

File: how_deep.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is a counter for the "depth" of empty lists.

"""
import random


def how_deep(list_struct):
    # this is the base case [] = 1
    if list_struct == []:
        return 1
    else:
        # this for each loop determines the deepest sublist/the sublist with the maximum amount of brackets
        max_depth = 0
        for sublist in list_struct:
            depth = how_deep(sublist)
            if depth > max_depth:
                max_depth = depth
        # then returns the deepest sublist + 1 since you have to add the most outer bracket
        return max_depth + 1


# the given starter code:
def make_list_structure(max_depth, p=.8):
    if max_depth and random.random() < p:
        new_list = []
        for i in range(5):
            sub_list = make_list_structure(max_depth - 1, p * .9)
            if sub_list is not None:
                new_list.append(sub_list)
        return new_list
    return None


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
