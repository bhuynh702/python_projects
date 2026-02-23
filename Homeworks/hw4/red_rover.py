"""

File: red_rover.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Date: October 2023
Description: This is a fun little game where you have 2 teams and move players from team to team til one of them wins... Took forever to code, but it was fun, I guess...

"""

if __name__ == '__main__':
    red_team = []
blue_team = []
red_input = ''
blue_input = ''

while red_input != "begin the game" and blue_input != 'begin the game':
   red_input = input("Who should we add to the Red team? ")
   blue_input = input("Who should we add to the Blue team? ")
   if red_input != "begin the game" and blue_input != 'begin the game':
       red_team.append(red_input)
       blue_team.append(blue_input)

while len(red_team) > 1 and len(blue_team) > 1:
   red_turn = input("Who should the Red team send over? ")
   while red_turn not in red_team:
       if red_turn == "display":
           print('The Red Team is composed of:')
           print(*red_team, sep=", ")
       elif red_turn not in red_team:
           print(red_turn, 'is not on the Red team. Try again.')
       red_turn = input("Who should the Red team send over? ")

   make_through = input("Did they make it through the line? ")
   if make_through == "yes":
       print(red_turn, "stays on the Red team.")
   elif make_through == "no":
       blue_team.append(red_turn)
       red_team.remove(red_turn)
       print(red_turn, "changes to the Blue team.")

   blue_turn = input("Who should the Blue team send over? ")
   while blue_turn not in blue_team:
       if blue_turn == "display":
           print('The Blue Team is composed of:')
           print(*blue_team, sep=", ")
       elif blue_turn not in blue_team:
           print(blue_turn, "is not on the Blue team. Try again.")
       blue_turn = input("Who should the Blue team send over? ")

   make_through = input("Did they make it through the line? ")
   if make_through == "yes":
       print(blue_turn, "stays on the Blue team.")
   elif make_through == "no":
       red_team.append(blue_turn)
       blue_team.remove(blue_turn)
       print(blue_turn, "changes to the Red team.")

if len(red_team) == 1:
   print("The Blue team has won!")
elif len(blue_team) == 1:
   print("The Red team has won!")
