"""
Mini-max Tic-Tac-Toe Player
File with the logic for the game
Author: Rafael Pacheco Ribeiro
"""

from board import *
from random import randrange

# Scoring constant values
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
        for score, square in zip(scores, squares):
            result.append((score, square))
        if player == consts["PLAYERX"]:
            return max(result)
        else:
            return min(result)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]
