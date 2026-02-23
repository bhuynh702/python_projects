"""

File: gandalf.py
Author: Brittany Huynh
E-mail: bhuynh4@gl.umbc.edu
Description: This file guesses which character you are from Lord of the Rings.

"""

race = input('What race are you? (human/dwarf/elf/maiar/hobbit) ')

if race.lower() == 'human': 
    human = input('Are you King of Gonder? ')
    if human == 'yes':
        print('You are Aragorn son of Arathorn.')
    elif human == 'no':
        frodo = input('Did you try to take the ring from Frodo? ')
        if frodo == 'yes':
            print('You are Boromir.')
        if frodo == 'no':
            print('You are probably Theoden.')
elif race.lower() == 'elf':
    matrix = input('Were you in the matrix? ')
    if matrix == 'yes':
        print('You are Elrond.')
    if matrix == 'no':
        print('You are Legolas.')
elif race.lower() == 'maiar':
    good_evil = input('Are you good or evil? ')
    if good_evil == 'good':
        print('You are Gandalf.')
    if good_evil == 'evil':
        ring = input('Did you forge the One Ring? ')
        if ring == 'yes':
            print('You are Sauron.')
        if ring == 'no':
            print('You are Saruman.')
elif race.lower() == 'hobbit':
    one_ring = input('Do you carry the One Ring? ')
    if one_ring == 'yes':
        print('You are Frodo Baggins.')
    if one_ring == 'no':
        gardener = input('Are you a gardener? ')
        if gardener == 'yes':
            print('You are Samwise.')
        if gardener == 'no':
            print('You are either Merry or Pippin.')
elif race.lower() == 'dwarf':
    print('You are Gimli, the son of Gloin.')
else:
    print('You are an orc, sorry about that')
