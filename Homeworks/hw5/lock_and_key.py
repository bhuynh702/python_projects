"""
File: lock_and_key.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: October 2023
Description: This file is a lock that unlocks if the key cuts and pins add up to 6.

"""

def lock_and_key(key_cuts, lock_pinning, minimum):
    if len(key_cuts) != len(lock_pinning): # if the lists have unequal num of elements,
                                            # the lock will NOT unlock
        return False
    else:
        for i in range(len(key_cuts)): # for every number in each given list,
            result = key_cuts[i] + lock_pinning[i] # the nums will be added together
                                                    # e.g. 2.1 will add to 4.1
            if (result < 6 - minimum) or (result > 6 + minimum): # if the result is OUTSIDE of the bounds
                                                            # (5.75,6.25) it was return false and NOT unlock
                return False
        return True # will return True as long as sum is in bounds


if __name__ == '__main__':
    if lock_and_key([2.1, 3.5, 2.7], [4.1, 2.5, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')

    if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')

    if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2, 3.2], 0.25):
        print('Unlocked')
    else:
        print('Still Locked')
