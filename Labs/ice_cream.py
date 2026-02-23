"""

File: ice_cream.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Description: This file tells you which ice cream flavors go well with which toppings.

"""

flavors = ["vanilla","strawberry", "chocolate"]
toppings = ["caramel", "marshmallow", "gummy bears"]


for flavor in flavors:
    if flavor == "strawberry":
        print(flavor, "is fine on its own")    
    else:
        for topping in toppings:
            print(flavor, "is tasty with", topping)
