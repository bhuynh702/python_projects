"""

File: factor_me.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Date: October 2023
Description: This a prime factorization generator.

"""

if __name__ == '__main__':

    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

num = int(input('Enter a number to factor: '))

factors_list = []

for i in prime_nums:
    while num % i == 0:
        num //= i

        factors_list.append(i)

if len(factors_list) == 0:
    print("We didn't find any factors", "\nThis part of the number couldn't be factored with primes less than 50:", num)
elif num != 1:
    print("The factors are: ", *factors_list, sep="*")
    print("This part of the number couldn't be factored with primes less than 50: ")
    print(num)
else:
    print("The factors are: ", *factors_list, sep="*")
