"""

File: burger_builder.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Date: October 2023
Description: This file is a burger builder, duh.

"""

if __name__ == '__main__':
    print("Welcome to burger builder!")
# Create an empty list to store the contents of the burger
burger_contents = []
# Set an initial value for the amt of cheese 
cheese_count = 0
# Ask for user input
add_toppings = input("What do you want to add? ")

# This while loop checks if the first input is not 'bottom bun'
while add_toppings.lower() != "bottom bun":
    print("You must start with the bottom bun!")
    add_toppings = input("What do you want to add? ")

# if input is 'bottom bun', then we proceed to ask what toppings they want to add to their burger
while add_toppings.lower() != "top bun": # the loop will continue to ask the question until the input is 'top bun'
    if add_toppings.lower() == "cheese":
        cheese_count += 1 # if input is cheese, we add how much cheese the user inputs
    elif add_toppings.lower() != "top bun":
        burger_contents.append(add_toppings) # we append (add) the toppings of choice to the empty list we made earlier
    add_toppings = input("What do you want to add? ")

# this is where the toppings are stored that aren't the burger or buns
condiments = []
for condiment in burger_contents:
    if (condiment not in condiments) and (condiment not in ['bottom bun','burger','top bun']):
        condiments.append(condiment)
# if user inputs 1 or more cheese slices, they will have a cheeseburger with however many slices they put
if cheese_count > 0:
    print (f"You have created a {cheese_count}-cheeseburger with the condiments:")
else:
    print("You have created a hamburger with the condiments:") # if user inputs no cheese, they have a hamburger

# if the length of the condiment list is 0, there are no condiments detected
if len(condiments) == 0:
    print("No Condiments")
else: # if the length of the condiment list is anything other than 0, it will print out what toppings they input 
    print(", ".join(condiments))
