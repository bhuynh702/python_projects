"""

File: cookies.py
Author: Brittany Huynh
Date: 09/12/2023
E-mail: bhuynh4@umbc.edu
Description: This file shows a recipe for cookies, depending on how many batches of cookies the user needs.

"""

num_cookies = float(input('How many batches of cookies do you want to make? '))

orig_flour = 2.25
orig_butter = 2.0
orig_sugar = 0.75
orig_brown_sugar = 0.75
orig_vanilla = 1.0
orig_baking_soda = 1
orig_salt = 1.0
orig_choc = 2.0

new_flour = (orig_flour * num_cookies)
new_butter = (orig_butter * num_cookies)
new_sugar = (orig_sugar * num_cookies)
new_brown_sugar = (orig_brown_sugar * num_cookies)
new_vanilla = (orig_vanilla * num_cookies)
new_baking_soda = (orig_baking_soda * num_cookies)
new_salt = (orig_salt * num_cookies)
new_choc = (orig_choc * num_cookies)

print('You will need: ')
print(new_flour, 'cups of flour')
print(new_butter, 'sticks of butter')
print(new_sugar, 'cups of granulated sugar')
print(new_brown_sugar, 'cups of brown sugar')
print(new_vanilla, 'teaspoon(s) of vanilla extract')
print(new_baking_soda, 'teaspoon(s) of baking soda')
print(new_salt, 'teaspoon(s) of salt')
print(new_choc, 'cups of chocolate chips')
print('Make sure to set a timer!')
