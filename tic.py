"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
from random import randrange

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

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
            score, dummy_tuple = mm_move(temp, provided.switch_player(player))
            squares.append(square)
            scores.append(score)
            temp = board.clone()
        result = []
        print scores
        for score, square in zip(scores, squares):
            result.append((score, square))
        if player == provided.PLAYERX:
            return max(result)
        else:
            return min(result)

#board = provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]])
#print board
#print mm_move(board, provided.PLAYERX)

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
