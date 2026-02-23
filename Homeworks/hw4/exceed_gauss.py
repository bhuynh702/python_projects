"""

File: exceed_gauss.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Description: This is a gauss sum calculator, that tells you when the gauss sum is equal to or greater than the number you chose.

"""

if __name__ == '__main__':
    number = int(input("Enter a number: "))

gauss_sum = 0
iter_count = 0

while gauss_sum < number:
    iter_count += 1
    gauss_sum += iter_count

print(f"After {iter_count} iterations, the gauss sum is {gauss_sum} which exceeds (or is equal to) the number {number}")
