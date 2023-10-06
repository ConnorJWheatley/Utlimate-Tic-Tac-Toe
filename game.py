import pygame
from constants import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1
        self.playing = True
        pygame.font.init()

    def render_board(self, surface):
        self.board.render(surface)