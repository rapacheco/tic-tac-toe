"""
Mini-max Tic-Tac-Toe Player
File with the logic for the game
Author: Rafael Pacheco Ribeiro
"""

from board import *
from random import randrange

# Set timeout, as mini-max can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {consts["PLAYERX"] : 1,
          consts["DRAW"] : 0,
          consts["PLAYERO"] : -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return (SCORES[board.check_win()], (-1, -1))

    else:
        temp = board.clone()
        empty_squares = board.get_empty_squares()
        squares = []
        scores = []
        for square in empty_squares:
            temp.move(square[0], square[1], player)
            score, dummy_tuple = mm_move(temp, switch_player(player))
            squares.append(square)
            scores.append(score)
            temp = board.clone()
        result = []
        # print(scores)
        for score, square in zip(scores, squares):
            result.append((score, square))
        if player == consts["PLAYERX"]:
            return max(result)
        else:
            return min(result)

board = TTTBoard(3, False, [[consts["EMPTY"], consts["EMPTY"], consts["EMPTY"]], [consts["PLAYERO"], consts["PLAYERX"], consts["PLAYERX"]], [consts["PLAYERO"], consts["EMPTY"], consts["EMPTY"]]])
print(board)
print(mm_move(board, consts["PLAYERX"]))

#PLAYERX = provided.PLAYERX
#PLAYERO = provided.PLAYERO
#EMPTY = provided.EMPTY
#board = provided.TTTBoard(3, board=[[PLAYERX, EMPTY, EMPTY],
#                                    [PLAYERO, PLAYERO, PLAYERX],
#                                    [PLAYERX, PLAYERX, PLAYERO]])
#print board
#print mm_move(board, PLAYERO), ". Expected: (some score, (1, 2))"
#
#board = provided.TTTBoard(3, board=[[EMPTY, PLAYERX, PLAYERO],
#                                    [EMPTY, PLAYERX, EMPTY],
#                                    [PLAYERX, PLAYERO, PLAYERO]])
#
#print board
#print mm_move(board, PLAYERX), ". Expected: (some score, (1, 2))"
#
#board = provided.TTTBoard(3, board=[[EMPTY, EMPTY, EMPTY],
#                                    [EMPTY, EMPTY, EMPTY],
#                                    [EMPTY, EMPTY, EMPTY]])
#
#print board
#print mm_move(board, PLAYERX), ". Expected: (some score, (1, 2))"


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
