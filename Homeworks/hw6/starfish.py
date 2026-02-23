"""

File: starfish.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is a starfish limb generator thingy.

"""


def starfish(leg_list, generations):
    # the param leg_list is the list that hold the inputted values
    # the base case: generations = 0 ends the function and returns the leg_list
    if generations == 0:
        return leg_list
    else:
        # this is a new list which holds the new values appended in the while loop
        new_legs = []
        # this while loops detects 5's in the given list
        while 5 in leg_list:
            leg_list.remove(5)  # removes them
            for z in range(5):
                new_legs.append(1)  # and appends 1, 5 times
        for i in range(len(leg_list)):
            leg_list[i] += 1  # then adds 1 to each value in the list
    # in the end it combines leg_list and the new_legs list and \
    # generations - 1: which is what allows the function to traverse/iterate (generation) amount of times
    # til it hits 0 and ends function
    return starfish(leg_list + new_legs, generations - 1)


# the given starter code which counts the amount of occurrences of each number in leg_list:
def count_starfish(leg_list):
    leg_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for x in leg_list:
        leg_counts[x] += 1
    return leg_counts


if __name__ == '__main__':
    print(count_starfish(starfish([1, 2, 3, 4, 5], 3)))
    print(count_starfish(starfish([2, 4, 5], 10)))
    print(count_starfish(starfish([5, 5, 5], 1)))
    print(count_starfish(starfish([1], 20)))
    print(count_starfish(starfish([5, 5, 5, 5, 5], 5)))

