import pygame
from constants import *
from board import Board

class Game:

    def __init__(self, ultimate_mode=False):
        self.ultimate_mode = ultimate_mode
        self.board = Board(ultimate_mode=ultimate_mode)
        self.player = 1
        self.playing = True
        pygame.font.init()

    def next_turn(self):
        self.player = 2 if self.player == 1 else 1

    def render_board(self, surface):
        self.board.render(surface)