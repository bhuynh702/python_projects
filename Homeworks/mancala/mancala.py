"""
File: mancala.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is the game mancala.

"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
NUM_CUPS = 6
num_marbles = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """

    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]

"""
this is my get_player function, it is called later in the run_game() function
"""
def get_player(num):
    if num == 1:
        player_1 = input("Player 1 please tell me your name: ")
        return player_1
    elif num == 2:
        player_2 = input("Player 2 please tell me your name: ")
    return player_2


"""
My take_turn() function is what controls the input, it implements my 2 helper functions
to check for an empty cup/invalid, and checks if the player can get a second turn 
it controls the calculation of each move, e.g. if the selected cup has 4 marbles,
the for i loop moves the 4 marbles over to the next 4 cups correctly 
"""
def take_turn(second_turn, player, marbles):
    move = int(input(f"{player}, what cup do you want to move? "))
    empty_cup = check_empty(move)

    while empty_cup:
        print("The cup you selected is empty or invalid, try again. ")
        move = int(input(f"{player}, what cup do you want to move? "))
        empty_cup = check_empty(move)

    user_cup = marbles[move]
    current_cup = move
    marbles[move] = 0

    for i in range(1, user_cup + 1):
        marbles[(move + i) % 14] += 1
        current_cup += 1 # for checking mancala
        current_cup = current_cup % 14

    landed_in_mancala = check_mancala(current_cup)
    if landed_in_mancala:
        print("Your stone landed in a mancala, go again...")
        return second_turn
    else:
        second_turn += 1
        return second_turn


"""
this is my check_empty() helper function which checks if the chosen cup has no marbles in it 
or if the selected cup does not exist within the bounds (1,6) and (8-13)
it is called in the take_turn() function above
"""
def check_empty(move):
    while (0 < move < 7) or (7 < move < 14) or move == 0 or move == 7:
        if num_marbles[move] == 0:
            return True # in this case True is returned as invalid or empty
        else:
            return False
    return True


"""
this is my check_mancala() helper function which check if the player's last stone lands in a mancala
it is called in my take_turn() function 
"""
def check_mancala(current_cup):
    landed_in_mancala = False
    if (current_cup == 0) or (current_cup == 7):
        landed_in_mancala = True
    return landed_in_mancala


"""
this is my winner() function to check who the winner is
if the top or bottom board has no marbles, 
it will return False and end the game 
"""
def winner(continue_turn, marbles):
    top_board = 0
    bottom_board = 0
    for i in range(1, 7):
        top_board += marbles[i]
    if top_board == 0:
        continue_turn = False

    for i in range(8, 14):
        for i in range(8, 14):
            bottom_board += marbles[i]
        if bottom_board == 0:
            continue_turn = False

    return continue_turn

"""
this is the function that displays the board 
"""

def show_board(player_1, player_2, marbles):
    all_cells = []
    for i in range(1, 7):
        current_cell = []
        current_cell.append("Cup   ")
        current_cell.append(f"    {i}")
        current_cell.append("Stones")
        current_cell.append(f"    {num_marbles[i]}")
        current_cell.append("      ")
        for i in range(BLOCK_HEIGHT - 1):
            current_cell.append(" " * BLOCK_WIDTH)
        all_cells.append(current_cell)

    for i in range(13, 7, -1):
        current_cell = []
        current_cell.append("Cup   ")
        current_cell.append(f"    {i}")
        current_cell.append("Stones")
        current_cell.append(f"    {num_marbles[i]}")
        current_cell.append("      ")
        for i in range(BLOCK_HEIGHT - 1):
            current_cell.append(" " * BLOCK_WIDTH)
        all_cells.append(current_cell)

    top_rows = all_cells[0:NUM_CUPS]
    bottom_rows = all_cells[NUM_CUPS:]

    first_mancala = []
    second_mancala = []
    for i in range(BLOCK_HEIGHT * 2 + 1):
        if i == 5:
            first_mancala.append(player_1)
            second_mancala.append(player_2)
        elif i == 7:
            first_mancala.append("Stones")
            second_mancala.append("Stones")
        elif i == 8:
            first_mancala.append(f"{num_marbles[0]}")
            second_mancala.append(f"{num_marbles[7]}")
        else:
            first_mancala.append(" " * BLOCK_WIDTH)
            second_mancala.append(" " * BLOCK_WIDTH)

    draw_board(top_rows, bottom_rows, first_mancala, second_mancala)


"""
this is the function that ties all of the previous functions together and 
allows the game to run 
"""
def run_game():
    player_1 = get_player(1)
    player_2 = get_player(2)

    current_player = 1
    continue_turn = True

    while continue_turn:
        show_board(player_1, player_2, num_marbles)
        if current_player % 2 == 1:
            current_player = take_turn(current_player, player_1, num_marbles)
            continue_turn = winner(continue_turn, num_marbles)
        elif current_player % 2 == 0:
            current_player = take_turn(current_player, player_2, num_marbles)
            continue_turn = winner(continue_turn, num_marbles)

        if not continue_turn:
            if current_player % 2 == 1:
                print(f"{player_1} is the winner! ")
            elif current_player % 2 == 0:
                print(f"{player_2} is the winner! ")


if __name__ == "__main__":
    run_game()

