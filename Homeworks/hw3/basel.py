"""

File: basel.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: 09/2023
Description: This file is a calculator using Euler's method.

"""

num_terms = int(input('Enter number of terms you want to sum: '))

total = 1

for i in range(1, num_terms):
    total += (1 / (i + 1) ** 2)
    
print('The approximation for',num_terms,'terms is',total)
