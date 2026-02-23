"""

File: tactego.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: November 2023
Description: This is Project 2 Tactego.

"""
import random


def open_file(file):
    """
    this function is what accesses the piece files
    and creates a list of numbers based on the
    contents of files small_game.pieces and basic.pieces
    """
    new_file = open(file, 'r')
    pieces = []
    for line in new_file:
        line = line.strip()
        line_list = line.split()
        for i in range(int(line_list[1])):
            pieces.append(line_list[0])
    new_file.close()
    return pieces


def piece_color(pieces, red_pieces_list, blue_pieces_list):
    """
    :param pieces: list of numbers and F
    :return: new list of pieces that have R or B in front of number or F
    """

    red_piece = "R"
    blue_piece = "B"
    for i in range(len(pieces)):
        red_pieces_list.append(red_piece + pieces[i])
        blue_pieces_list.append(blue_piece + pieces[i])
    # the above lines of code create the pieces name like B3, R1, RF, etc
    random.shuffle(red_pieces_list)
    random.shuffle(blue_pieces_list)


# these randomly shuffle the pieces in the list based on the seed


def make_board(the_length, the_width):
    board = []
    space = ''
    for i in range(the_length):
        row = []
        for j in range(the_width):
            row.append(space)
        board.append(row)
    return board


def put_pieces_in(red_list, blue_list, board_width, board):
    """
    :param red_list: given list of numbers and F for the pieces
    :param blue_list: given list of numbers and F for the pieces
    :param board: empty board / make_board function
    :param board_width: given board width
    :return:
    """
    red_counter = 0
    blue_counter = 0
    row = 0
    last_row = len(board) - 1

    while red_counter < len(red_list):
        red_index = red_counter % board_width
        board[row][red_index] = red_list[red_counter]
        red_counter += 1
        if red_counter % board_width == 0:
            row += 1

    while blue_counter < len(blue_list):
        blue_index = blue_counter % board_width
        board[last_row][blue_index] = blue_list[blue_counter]
        blue_counter += 1
        if blue_counter % board_width == 0:
            last_row -= 1
    return board


def display_board(board, width, length):
    """
    :param board: the 2D list of all the red and blue
    pieces e.g. ['R5', 'R3', 'R2'...]
    :param length: the given length (vertical size) of board
    :param width: the given width (horizontal size) of board
    :return: the final formatted board
    """
    # this is a tab that creates the indentation of the first horizontal line
    print("\t", end="")
    # this 'for i' loop creates the spaces inbetween the numbers (0, 1, 2, 3)
    for i in range(width):
        print(i, end='\t')
    print()
    # this 'for j' loop is what prints the vertical numbers 0-5
    for j in range(length):
        print(j, end="\t")
        # the nested loop is what prints the pieces
        for piece in board[j]:
            print(piece, end="\t")
        print()


def move_pieces(the_board, user_piece, user_position):
    """
    :param the_board: the final with all the pieces
    :param user_piece: the user inputted selected piece
    :param user_position: the user inputted move
    :return: the board after updating the move
    """
    piece_selected = user_piece.split(" ")
    position_move = user_position.split(" ")
    # index of selected piece
    a = int(piece_selected[0])
    b = int(piece_selected[1])
    # index of selected move
    x = int(position_move[0])
    y = int(position_move[1])

    if 0 <= a <= (length - 1) and 0 <= x <= (length - 1):
        if 0 <= b <= (width - 1) and 0 <= y <= (width - 1):
            current_piece = the_board[a][b]
            move_spot = the_board[x][y]
        else:
            print("That is not a valid move, please select again.")
            return
    else:
        print("That is not a valid move, please select again. ")
        return

    check_valid = check_move(a, b, x, y, current_piece, move_spot)
    if not check_valid:
        return

    if move_spot == '':
        the_board[x][y] = current_piece
        the_board[a][b] = ''
        return the_board
    elif current_piece[0] != move_spot[0]:
        combat(current_piece, move_spot, the_board, a, b, x, y)

        return the_board


def check_move(index1, index2, move_index1, move_index2, current, move):
    """
    :param index1: first index of selected piece
    :param index2: second index of selected piece
    :param move_index1: first index of selected move
    :param move_index2: second index of selected move
    :param current: the piece at the index
    :param move: the move to move piece to
    :return: valid_action - boolean flag that returns false if the conditions are not met
    """
    lowest_valid1 = index1 - 1
    highest_valid1 = index1 + 1
    lowest_valid2 = index2 - 1
    highest_valid2 = index2 + 1
    # highest and lowest possible moves that the piece can go into

    valid_action = True

    if current == '':
        print("That is not a valid move, please select again.")
        valid_action = False

    elif current[1] == "F":
        print("A flag cannot move, select again. ")
        valid_action = False

    if not lowest_valid1 <= move_index1 <= highest_valid1 or not lowest_valid2 <= move_index2 <= highest_valid2:
        print("You can only move left, right, up, down, o diagonal one block, select again.")
        valid_action = False

    if ('B' in current and 'B' in move) or ('R' in current and 'R' in move):
        print("You cannot attack your own pieces, select again.")
        valid_action = False

    return valid_action


def combat(attacking_piece, defending_piece, board, selected_index1, selected_index2, move_index1, move_index2):
    """
    :param attacking_piece: the selected piece
    :param defending_piece: where the selected piece is moving into
    :param board: updated board with all pieces and recent moves
    :param selected_index1: first index of selected piece
    :param selected_index2: second index of selected piece
    :param move_index1: first index of selected move
    :param move_index2: first index of selected move
    """
    if defending_piece[1] == "F":
        board[move_index1][move_index2] = attacking_piece
        board[selected_index1][selected_index2] = ''
    else:
        attack_strength = int(attacking_piece[1])
        defending_strength = int(defending_piece[1])

        if attack_strength >= defending_strength:
            board[move_index1][move_index2] = attacking_piece
            board[selected_index1][selected_index2] = ''
        else:
            board[selected_index1][selected_index2] = ''


def continue_game(the_board):
    """
    :param the_board: updated board with recent moves
    :return: boolean flag that's true if conditions are met
    """
    cont_game = False
    count = 0

    for row in the_board:
        if 'RF' in row:
            count += 1
        if 'BF' in row:
            count += 1
        if count == 2:
            cont_game = True
    return cont_game


def declare_winner(the_board):
    """
    :param the_board: board after the flag has been captured
    :return red_win: if red is detected to win then the red win is returned
            blue_win: if blue is detected to win then blue win is returned
    """
    for i in the_board:
        if 'RF' in i:
            red_win = "Red Team wins!"
            return red_win
        elif 'BF' in i:
            blue_win = "Blue Team wins!"
            return blue_win


def tactego(pieces_file, board_length, board_width):
    """
    :param pieces_file: user selected file
    :param board_length: length of board
    :param board_width: width of board
    :return:
    """
    red = []
    blue = []
    turn = 1
    select_piece = "Select a piece to move by position >> "
    select_position = "Select a position to move the piece >> "
    # empty red and blue lists, turn counter, inputs

    pieces = open_file(pieces_file)
    piece_color(pieces, red, blue)
    board = make_board(board_length, board_width)
    put_pieces_in(red, blue, board_width, board)
    not_end = continue_game(board)
    # calls all of previous functions and displays entire final board

    while not_end:
        if turn % 2 == 1:
            display_board(board, board_width, board_length)
            piece_selected = input(select_piece)
            position_move = input(select_position)
            move_pieces(board, piece_selected, position_move)
            not_end = continue_game(board)
        elif turn % 2 == 0:
            display_board(board, board_width, board_length)
            piece_selected = input(select_piece)
            position_move = input(select_position)
            move_pieces(board, piece_selected, position_move)
            not_end = continue_game(board)

    winner = declare_winner(board)
    print(winner)


if __name__ == '__main__':
    random.seed(input('What is seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego(file_name, length, width)
