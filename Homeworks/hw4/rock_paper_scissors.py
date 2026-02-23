"""

File: rock_paper_scissors.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Date: October 2023
Description: This a rock-paper-scissors game with Python!

"""

import sys
from random import choice, seed

if len(sys.argv) >= 2:
   seed(sys.argv[1])
   if __name__ == '__main__':

       from random import choice

user_choice = input("Enter rock, paper, or scissors to play, stop to end: ").lower()

while user_choice != "stop":
    if user_choice not in ["rock", "paper", "scissors"]:
        print("You need to select rock, paper, or scissors.")
    else:
        the_choice = choice(["rock", "paper", "scissors"])
        
        if user_choice == the_choice:
            print(f"Both {user_choice}, there is a tie.")
        elif (user_choice == "rock" and the_choice == "scissors"):
            print("Rock crushes scissors, you win.")
        elif (user_choice == "scissors") and the_choice == "paper":
            print("Scissors cut paper, you win")
        elif (user_choice == "paper") and (the_choice == "rock"):
            print("Paper covers rock, you win.")
        
        elif (user_choice == "scissors" and the_choice == "rock"):
            print("Rock crushes scissors, you lose.")
        elif (user_choice == "paper") and the_choice == "scissors":
            print("Scissors cut paper, you lose")
        elif (user_choice == "rock") and (the_choice == "paper"):
            print("Paper covers rock, you lose.")
        
    user_choice = input("Enter rock, paper, or scissors to play, stop to end: ").lower()
