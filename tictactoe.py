import os

import pygame
from pygame.locals import *

from logic import *

# constants
BORDER = 15
TILE_SIZE = 120
CELLS = 3
BLACK = (0, 0, 0)
RED = (255, 30, 30)
BACK = (187, 173, 160)
TILE = (157, 143, 130)

def main():
    """
    Function to run the graphics and main logic
    """
    game = TTTBoard(3)
    main = Main(game)
    while not main._done:
        main.loop()

class Main:
    """
    Class to instantiate the graphics of the game
    and to execute its logic
    """

    def __init__(self, game):
        # instantiate Pygame library
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        if pygame.font is None:
            print("Warning, fonts disabled")
        if pygame.mixer is None:
            print("Warning, sound disabled")
        pygame.display.set_caption("Tic-Tac-Toe Minimax!")

        # instantiate data members
        self._game = game
        self._player = consts["PLAYERX"]
        self._rows, self._cols = CELLS, CELLS
        self._coord = (-1, -1)
        self._font = pygame.font.SysFont("Arial", 100)
        self._clock = pygame.time.Clock()
        self._end = False
        self._done = False

        # instantiante data members related to graphics
        self._screen = pygame.display.set_mode((BORDER + self._cols * (BORDER + TILE_SIZE), BORDER + self._rows * (BORDER + TILE_SIZE)))
        self._screen.fill(BACK) # background color for the board
        self._tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self._tile.fill(TILE) # background color for the tile

        # surfaces for the X tile
        self._xtile = self._tile.copy()
        pygame.draw.line(self._xtile, BLACK, (TILE_SIZE / 10, TILE_SIZE / 10), (TILE_SIZE / 10 * 9, TILE_SIZE / 10 * 9), 10)
        pygame.draw.line(self._xtile, BLACK, (TILE_SIZE / 10, TILE_SIZE / 10 * 9), (TILE_SIZE / 10 * 9, TILE_SIZE / 10), 10)

        # surfaces for the O tile
        self._otile = self._tile.copy()
        pygame.draw.circle(self._otile, BLACK, (int(TILE_SIZE / 2), int(TILE_SIZE / 2)), int(TILE_SIZE / 2.5), 10)


    def draw(self):
        """
        Draws the game into the canvas
        """
        if self._end:
            # If game has ended, print winner (or draw) in the screen
            result = self._game.check_win()
            if result == consts["PLAYERX"]:
                string = "X WINS"
            elif result == consts["PLAYERO"]:
                string = "O WINS"
            else:
                string = "DRAW"
            phrase = self._font.render(string, True, RED)
            size = self._font.size(string)
            width = TILE_SIZE * 3 + BORDER * 4
            self._screen.blit(phrase, ((width - size[0]) / 2, (width - size[1]) / 2))

        else:
            for row in range(self._rows):
                for col in range(self._cols):
                    # Create a tile and draw it on the board
                    top = BORDER + row * (TILE_SIZE + BORDER)
                    left = BORDER + col * (TILE_SIZE + BORDER)

                    # If there is a X or an O, draw it on tile
                    if self._game.square(row, col) == consts['PLAYERX']:
                        self._screen.blit(self._xtile, (top, left))
                    elif self._game.square(row, col) == consts['PLAYERO']:
                        self._screen.blit(self._otile, (top, left))
                    else:
                        self._screen.blit(self._tile, (top, left))

    def loop(self):
        """
        Method that runs the main loop for the graphics
        """
        # Check for winning/losing/draw conditions
        result = self._game.check_win()
        if result:
            self._end = True

        # Pause the game for one second before player O move
        if self._player == consts["PLAYERO"]:
            pygame.time.wait(1000)
            self.enemy_move()

        for event in pygame.event.get():

            # If press EXIT button, exit the game
            if event.type == pygame.QUIT:
                self._done = True

            # Get the position of the mouse when click
            if event.type == pygame.MOUSEBUTTONDOWN and self._player == consts["PLAYERX"]:
                # Get X coordinate
                x = int(pygame.mouse.get_pos()[0] / (TILE_SIZE + BORDER))
                xoff = pygame.mouse.get_pos()[0] % (TILE_SIZE + BORDER)
                if xoff <= BORDER:
                    x = -1
                # Get y coordinate
                y = int(pygame.mouse.get_pos()[1] / (TILE_SIZE + BORDER))
                yoff = pygame.mouse.get_pos()[1] % (TILE_SIZE + BORDER)
                if yoff <= BORDER:
                    y = -1
                # Update coordinate
                self._coord = (x, y)

            # Mark an X on the clicked tile, if valid
            if event.type == pygame.MOUSEBUTTONUP and self._player == consts["PLAYERX"]:
                if -1 not in self._coord:
                    self._game.move(self._coord[0], self._coord[1], consts["PLAYERX"])
                    self._player = switch_player(self._player)
                self._coord = (-1, -1)

        self.draw()
        pygame.display.flip()

    def enemy_move(self):
        """
        Make a move for the O player
        """
        dest = mm_move(self._game, consts["PLAYERO"])[1]
        self._game.move(dest[0], dest[1], consts["PLAYERO"])
        self._player = switch_player(self._player)

if __name__ == "__main__":
    main()
