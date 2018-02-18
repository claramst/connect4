# This file is the primary entry point for the web application and handles the
# high level game interactions

import numpy as np
import app.game.gameplay as gameplay

# Global variables initialized at startup
# Note that the board contains integer values: 0=empty, 1=human, 2=computer
HUMAN = 1
COMPUTER = 2
N = 6
the_board = np.zeros((N, N), dtype=np.int)
the_message = ["no message"]
the_game_is_over = [False]
# this must be changed to true within a function to end game

def get_board():
    """
    :return: return a reference to the board
    """
    return the_board


def get_message():
    """
    :return: return the current message
    """
    return the_message[0]


def start_new_game():
    """
    Clear the contents of the board ready for a new game
    """
    the_board.fill(0)
    the_message[0] = "no message"
    the_game_is_over[0] = False
    return


def next_human_move_and_computer(column):
    """
    Accept the next human move:
        1. Check move is valid
        2. update board
        3. Decide next computer move and update board
        4. Return any messages
    :param column: the column that the human chose
    :return:
    """
    print("next human move = " + str(column))

    if the_game_is_over[0]:  # the_game_is_over's 0th value will have been changed
        the_message[0] = "The game is over"
        return

    if not gameplay.is_human_move_valid(the_board, column):
        the_message[0] = "Invalid move"
        return

    over, message = gameplay.make_human_move(the_board, column)
    the_game_is_over[0] = over
    the_message[0] = message
    if 4 == gameplay.max_length_for_player(the_board, HUMAN):
        the_game_is_over[0] = True
        the_message[0] = "human wins, yay"
        return

    over, message = gameplay.make_computer_move(the_board)
    the_game_is_over[0] = over
    the_message[0] = message
    if 4 == gameplay.max_length_for_player(the_board, COMPUTER):
        the_game_is_over[0] = True
        the_message[0] = "computer wins, yay"
    return

