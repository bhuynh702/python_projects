"""
File: minor_key.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: October 2023
Description: This is a musical minor scale calculator.

"""

musical_notes = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F',
                 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']
steps = [2, 1, 2, 2, 1, 3, 1]

# this function takes the input and checks if it includes 'flat'
def turn_flat(note):
    if 'flat' in note:
        new_note = note.split()[0] + '\u266d' #then turns flat into the flat symbol
    else:
        new_note = note # if it doesn't have 'flat' it will just be a note

    return new_note

def note_index(note):
    if note in musical_notes: # if note is in the list of musical notes
        for i in range(len(musical_notes)): # the for loop iterates through each string
                                        # in the musical notes list
            if note == musical_notes[i]: # and checks if i is in the list and matches it's index
                return i
    else:
        print("There is no starting note",note) #if it's not in the list it will print this out
        return False

def minor_scale(note):
    index = note_index(note) #we call the last function
    print(musical_notes[index], end=' ') # this prints out the input first
    for x in steps: # this for loops iterates through each num in the steps list
        print(musical_notes[(index + x) % len(musical_notes)], end=' ') #then adds each num in the steps list
                                    # to the index of the musical note mod divisions it by the length
                                # so that output will stay within the bounds of the length of the musical
                                                    # notes list
        index = (index + x) % len(musical_notes) # we declare the variable index again

    print()


if __name__ == '__main__':

    starting_note = input("Enter a starting note (C, D flat): ")
    while starting_note != 'quit':
        flat_note = turn_flat(starting_note)
        minor_scale(flat_note)
        starting_note = input("Enter a starting note: ")
