# This file contains gameplay and game rules
import random

def is_human_move_valid(board, column):
    """
    Check that this is a valid human move
    :param board:
    :param column:
    :return: Is the move valid, True/False
    """
    if board[0, column] > 0:
        return False
    return True


def first_empty_cell_in_column(board, column):
    row = 5
    while row >= 0:
        if board[row, column] == 0:
            return row
        else:
            row = row - 1
        # go to while
    return -1


def make_human_move(board, column):
    """
    Insert the human move
    :param board:
    :param column:
    :return: game_over, message
    """
    row = first_empty_cell_in_column(board, column)
    if row < 0:
        return False, "invalid move"
    else:
        board[row, column] = 1
    return False, "No message"  # same as bottom lines in make_computer_move


def make_computer_move(board):
    empty = []
    for c in range(6):
        if board[0, c] == 0:
            empty.append(c)
    r = random.randint(0, len(empty)-1) # for randint end points included
    column = empty[r]
    print("next computer move = " + str(column))

    row = first_empty_cell_in_column(board, column)
    if row < 0:
        return False, "invalid move"
    else:
        board[row, column] = 2
        the_message = "Your turn"
        over = False
        return over, the_message
