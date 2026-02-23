"""

File: detector.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: 09/2023
Description: This file tells you how many diphthongs are in the word that you enter.

"""

word = input('Tell me a word you wish to check for diphthongs: ').lower()

vowels = ['a','e','i','o','u']

diph_count = 0
qu_check = True

for i in range(len(word)-1):
    if qu_check:
        if word[i] in vowels:
            if word[i +1 ] in vowels:
                diph_count += 1
    qu_check = True
    if word[i] == 'q':
        if word[i+1] == 'u': 
            qu_check = False
print(f"There are {diph_count} diphthongs in {word}.")
