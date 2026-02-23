"""

File: super.py
Author: Brittany Huynh
Date: 09/12/2022
E-mail: bhuynh4@umbc.edu
Description: This file tells if you're cool or not whether you're a villain or superhero.

"""

hero_villain = input("Are you a hero or villain?")

if hero_villain == " villain":
    name = input("What is your name?")
    print( name, "sounds pretty evil!")
if hero_villain == " hero":
    people = int(input("How many people have you saved?"))
    if people < 10:
        print("Go on more patrols!")
    
