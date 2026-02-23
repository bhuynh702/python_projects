"""

Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: December 2023
Description: This is Project 3 of CMSC201, Retriever Bell, a switchboard phone system.

"""
import json

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


def add_switchboard(switchboards, area_code):
    """
    sample input: switch-add 443

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param area_code: given area code (e.g. 443)
    :return: nothing
    """
    # if area_code is not already in switchboards,
    # then create the switchboard to that area code with the 'phone_numbers' dict and 'trunk_lines' list
    if area_code not in switchboards:
        switchboards[area_code] = {'phone_numbers': {}, 'trunk_lines': []}
    else:
        print("Area code is already in switchboard, enter a different area code.")
    pass


def connect_switchboards(switchboards, area_1, area_2):
    """
    sample input: switch-connect 443 202

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param area_1: first area code given (e.g. 443)
    :param area_2: second area code given (e.g. 202)
    :return: nothing
    """
    # if the area codes are found in the switchboard
    # then the area codes are added to each other's trunk lines
    if area_1 in switchboards and area_2 in switchboards:
        switchboards[area_1]['trunk_lines'].append(area_2)
        switchboards[area_2]['trunk_lines'].append(area_1)
    else:
        print("One or both of the area codes provided were not found in the switchboard. Enter valid area codes. ")
    pass


def add_phone(switchboards, area_code, phone_number):
    """
    sample input: phone-add 443-123-4567

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param area_code: given area code (e.g. 443)
    :param phone_number: phone numbers following the area code (e.g. 1234567)
    :return: nothing
    """
    # if the phone number is already found in the 'phone_numbers' key of the switchboards dict
    # then lets the user know
    if phone_number in switchboards[area_code]['phone_numbers']:
        print("The phone number already exists within the area code.")
    else:
        # if not then the provided number are added to the 'phone_numbers' key's value
        switchboards[area_code]['phone_numbers'][str(phone_number)] = []
        # and creates an empty list to store the connected phone numbers
    pass


def save_network(switchboards, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(switchboards, json_file)

    pass


def load_network(file_name):
    """
    :param file_name: the name of the file to load.
    :return: you must return the new switchboard network.  If you don't, then it won't load \
    properly.
    """
    with open(file_name, 'r') as file:
        data = json.load(file)

    switchboards = data
    return switchboards

    pass


def start_call_helper(switchboards, start_area, end_area, visited):
    """
    sample input: start-call 443-123-4567 202-123-4321

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param start_area: the first provided area code (e.g. 443)
    :param end_area: the second provided area code (e.g. 202)
    :param visited: dictionary that holds the visited phone numbers for this helper function
    (visited = {} is created in start_call function)
    :return: True/False
    """
    if start_area == end_area:
        return True
    # this the base case, if the recursive call reaches the condition of the base case,
    # this function returns True which is used to determine the connection in start_call
    visited[start_area] = True
    # if the start_area passes the base case, then we set the start_area to visited

    for next_area in switchboards[start_area]['trunk_lines']:
        # this for loop traverses through the trunk lines of the start_area
        if not visited[next_area]:
            # if the trunk line has not been visited yet
            restart_search = start_call_helper(switchboards, next_area, end_area, visited)
            # recursive call on the trunk line, we set the trunk line(next_area) to start_area
            # and repeats the process
            if restart_search == True:
                # if the base case is True
                return True
                # then the function returns True

    visited[start_area] = False
    # if there's no connection found during the recursive process, the function returns False
    return False
    pass


def start_call(switchboards, start_area, start_number, end_area, end_number):
    """
    sample input: start-call 443-123-4567 202-123-4321

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param start_area: the first area code provided (e.g. 443)
    :param start_number: the first provided number (e.g. 1234567)
    :param end_area: the second provided area code (e.g. 202)
    :param end_number: the second provided number (e.g. 1234321)
    :return: nothing
    """
    visited = {}
    # set visited to empty dict to hold visited area codes
    for area in switchboards:
        visited[area] = False
        # set each area to be False/unvisited initially
        # so the helper function can change the condition if True or False
    if start_call_helper(switchboards, start_area, end_area, visited) == True:
        # if start_call_helper returns True
        print(f"{start_area}-{start_number} and {end_area}-{end_number} are now connected.")
        switchboards[start_area]['phone_numbers'][str(start_number)].append(str(end_area) + HYPHEN + str(end_number))
        switchboards[end_area]['phone_numbers'][str(end_number)].append(str(start_area) + HYPHEN + str(start_number))
        # then the phone numbers are connected, this is done by appending the
        # phone numbers to each other's 'phone-numbers' key
    else:
        print(f"{start_area}-{start_number} and {end_area}-{end_number} were not connected.")
        # else then this statement prints out
    pass


def end_call(switchboards, start_area, start_number):
    """
    sample input: end-call 443-123-4567

    :param switchboards: switchboards that holds area codes, phone numbers,
    connected phone numbers, etc.
    :param start_area: the area code provided (e.g. 443)
    :param start_number: the number following the area code (e.g. 1234567)
    :return: nothing
    """
    # if the provided phone number is connected to another number (i.e. list is not empty)
    if switchboards[start_area]['phone_numbers'].get(str(start_number)) != []:
        # set a variable equal to the connected phone list
        connected_phone_list = switchboards[start_area]['phone_numbers'][str(start_number)]
        # set a variable equal to the element inside the list
        connected_phone = connected_phone_list[0]

        # set equal to empty list to remove the connected phone number
        switchboards[start_area]['phone_numbers'][str(start_number)] = []
        # split the hyphen
        connected_phone_split = connected_phone.split('-')
        # set end_area variable equal to first index of spliced phone number, which is
        # the area code of the phone number connected to the provided number
        end_area = connected_phone_split[0]
        # end_number would be second index of spliced string/the connected phone number without area code
        end_number = connected_phone_split[1]
        # set the other phone number's list to empty, I casted the end_area to an integer bc it's a string
        switchboards[int(end_area)]['phone_numbers'][end_number] = []
        print("Hanging up...\nConnection Terminated.")
    else:
        # if no connected phones are found then this line is printed out:
        print("Unable to disconnect. The provided number is not in use.")
    pass


def display(switchboards):
    # this the formatting for the display command
    for area_code in switchboards:
        print(f"Switchboard with area code: {area_code}")
        print("\tTrunk lines are:")
        if switchboards[area_code]['trunk_lines'] != []:
            for connection in switchboards[area_code]['trunk_lines']:
                print("\t\tTrunk line connection to:", connection)
        print("\tLocal phone numbers are: ")
        if switchboards[area_code]['phone_numbers'] != {}:
            for phone_number in switchboards[area_code]['phone_numbers']:
                if switchboards[area_code]['phone_numbers'][phone_number] != []:
                    print(f"\t\tPhone with number: {phone_number} is connected to {switchboards[area_code]['phone_numbers'][phone_number][0]}.")
                else:
                    print(f"\t\tPhone with number: {phone_number} is not in use. ")

    pass


if __name__ == '__main__':
    switchboards = {}
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            connect_switchboards(switchboards, area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            add_switchboard(switchboards, int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code, phone_number)
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            save_network(switchboards, split_command[1])
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            switchboards = load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))
            start_call(switchboards, src_area_code, src_number, dest_area_code, dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))
            end_call(switchboards, area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')
