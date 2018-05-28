import os
# from random import choice, randint, randrange
# from math import sqrt, atan, degrees

import pygame
from pygame.locals import *

from tic import *

# constants
BORDER = 15
TILE_SIZE = 120
CELLS = 3
BACK = (187, 173, 160)
TILE = (157, 143, 130)

def main():
    """
    Function to run the graphics and main logic
    """
    game = Main()
    while not game._done:
        game.loop()

# def load_image(file, colorkey=None, size=(50, 50)):
#     fullname = os.path.join("images", file)
#     img = pygame.image.load(fullname)
#     img = img.convert()
#     if colorkey is not None:
#         if colorkey is -1:
#             colorkey = img.get_at((0,0))
#         img.set_colorkey(colorkey, RLEACCEL)
#     return pygame.transform.scale(img, size)
#
# def load_sound(name, music=False):
#     class NoneSound:
#         def play(self): pass
#     if music:
#         folder = "music"
#     else:
#         folder = "sounds"
#     fullname = os.path.join(folder, name)
#     return pygame.mixer.Sound(fullname)
#
# def load_font(file, size):
#     if file is not None:
#         fullname = os.path.join("fonts", file)
#     else:
#         fullname = None
#     return pygame.font.Font(fullname, size)

class Main:
    """
    Class to instantiate the graphics of the game
    and to execute its logic
    """

    def __init__(self):
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
        self._rows, self._cols = CELLS, CELLS
        self._screen = pygame.display.set_mode((BORDER + self._cols * (BORDER + TILE_SIZE), BORDER + self._rows * (BORDER + TILE_SIZE)))
        self._clock = pygame.time.Clock()
        self._done = False

    def draw(self):
        """
        Draws the game into the canvas
        """
        self._screen.fill(BACK)
        for row in range(self._rows):
            for col in range(self._cols):
                tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
                tile.fill(TILE)

                top = BORDER + row * (TILE_SIZE + BORDER)
                left = BORDER + col * (TILE_SIZE + BORDER)
                self._screen.blit(tile, (top, left))

                # if num != 0:
                #     if num in [2, 4]:
                #         label = self._font.render(str(num), True, FONT)
                #     else:
                #         label = self._font.render(str(num), True, FONT2)
                #     label_size = self._font.size(str(num))
                #     offset = BORDER / 2 - 2
                #     self._screen.blit(label, (top + (TILE_SIZE - label_size[0]) / 2, left - offset + (TILE_SIZE - label_size[1]) / 2 + offset / 2))

    def loop(self):
    """
    Method that runs the main loop for the graphics
    """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True

        self.draw()
        pygame.display.flip()



if __name__ == "__main__":
    main()
