import pygame

from constants import *

class Board:

    def __init__(self):
        self.squares = [[0,0,0] for row in range(SQR_SIZE)]
        self.main_linewidth = 2
        self.sub_linewidth = 2

        self.left_vert_line = WIDTH * (1/3)
        self.right_vert_line = WIDTH * (2/3)
        self.top_hztl_line = HEIGHT * (1/3)
        self.btm_hztl_line = HEIGHT * (2/3)

    def __str__(self):
        s = ''
        for row in range(SQR_SIZE):
            for col in range(SQR_SIZE):
                sqr = self.squares[row][col]
                s += str(sqr)
        return s

    def render(self, surface): 
        for row in range (SQR_SIZE):
            for col in range (SQR_SIZE):
                square = self.squares[row][col]

        print(self.squares)

        # main board - vertical
        pygame.draw.line(surface, LINE_COLOUR, (self.left_vert_line, 0), (self.left_vert_line, HEIGHT), self.main_linewidth)
        pygame.draw.line(surface, LINE_COLOUR, (self.right_vert_line, 0), (self.right_vert_line, HEIGHT), self.main_linewidth)

        # main board - horizontal
        pygame.draw.line(surface, LINE_COLOUR, (0, self.top_hztl_line), (WIDTH, self.top_hztl_line), self.main_linewidth)
        pygame.draw.line(surface, LINE_COLOUR, (0, self.btm_hztl_line), (WIDTH, self.btm_hztl_line), self.main_linewidth)

    def valid_sqr(self, xclick, yclick):
        xpos, ypos = xclick, yclick
        print("xpos is: ", xpos)
        print("ypos is: ", ypos)
        xpos_valid = False
        ypos_valid = False

        if xpos < (self.left_vert_line - self.main_linewidth) or xpos > (self.left_vert_line + self.main_linewidth) and xpos < (self.right_vert_line - self.main_linewidth) or xpos > (self.right_vert_line + self.main_linewidth):
            xpos_valid = True
        if ypos < (self.top_hztl_line - self.main_linewidth) or ypos > (self.top_hztl_line + self.main_linewidth) and ypos < (self.btm_hztl_line - self.main_linewidth) or ypos > (self.btm_hztl_line + self.main_linewidth):
            ypos_valid = True

        if xpos_valid and ypos_valid:
            return True
        else:
            return False
