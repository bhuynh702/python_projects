"""
File: quasi_palindrome.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: October 2023
Description: This is a quasi palindrome calculator.

"""
def quasi_palindrome(word, k):
    """
        think about counting the number of errors
        i = 3
        L = 7
        7 - 1 - 3 = 3
        racecar
    """
    # we set a counter for the num of errors
    errors = 0
    for i in range(len(word) // 2): # i honestly don't rlly know how this part of the
                                # the func works i just got it from hamilton's github
        if word[i] != word[len(word) - 1 - i]:
            errors += 1

    if errors <= allowed_errors: # if the amt of counted errors is less than or
                    # equal to the allowed errors
        return True # it returns true
    else:
        return False # if not it returns false


if __name__ == '__main__':
    flag = True # boolean here to run the while loop with 2 inputs and input doesnt equal quit 

    while flag:
        user_input = input("What word do you want to check? ")
        if user_input.lower() == 'quit':
            flag = False
        else:
            allowed_errors = int(input("How many errors do you want to allow? "))
            if quasi_palindrome(user_input, allowed_errors):
                print(f"It was a {allowed_errors}-quasi-palindrome!")
            else:
                print(f"It was not a {allowed_errors}-quasi-palindrome!")
