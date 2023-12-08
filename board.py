import pygame

from constants import *
from board_dimensions import BoardDimensions

class Board:

    def __init__(self, board_dims=None, linewidth=6, ultimate_mode=False):
        self.squares = [([0] * SQR_SIZE) for row in range(SQR_SIZE)]

        self.board_dims = board_dims
        if not board_dims:
            self.board_dims = BoardDimensions(WIDTH, 0, 0)

        # used for creating shapes
        self.linewidth = linewidth
        self.offset = self.board_dims.sqsize * 0.2
        self.radius = (self.board_dims.sqsize // 2) * 0.75

        if ultimate_mode:
            self.create_ultimate_board()

        self.active = True
        self.brd_winner = -1
        self.tie_sqr = 0

    def create_ultimate_board(self):
        for row in range(SQR_SIZE):
            for col in range(SQR_SIZE):

                size = self.board_dims.sqsize
                xcor, ycor = self.board_dims.xcor + (col * self.board_dims.sqsize), self.board_dims.ycor + (row * self.board_dims.sqsize)
                board_dims = BoardDimensions(size=size, xcor=xcor, ycor=ycor)
                linewidth = self.linewidth - 5

                self.squares[row][col] = Board(board_dims=board_dims, linewidth=linewidth, ultimate_mode=False)

    def render(self, surface): 
        for row in range(SQR_SIZE):
            for col in range(SQR_SIZE):
                sqr = self.squares[row][col]
                if isinstance(sqr, Board): sqr.render(surface)

        # vertical lines
        pygame.draw.line(surface, LINE_COLOUR, (self.board_dims.xcor + self.board_dims.sqsize, self.board_dims.ycor), (self.board_dims.xcor + self.board_dims.sqsize, self.board_dims.ycor + self.board_dims.size), self.linewidth)
        pygame.draw.line(surface, LINE_COLOUR, (self.board_dims.xcor + self.board_dims.size - self.board_dims.sqsize, self.board_dims.ycor), (self.board_dims.xcor + self.board_dims.size - self.board_dims.sqsize, self.board_dims.ycor + self.board_dims.size), self.linewidth)

        # horizontal lines
        pygame.draw.line(surface, LINE_COLOUR, (self.board_dims.xcor, self.board_dims.ycor + self.board_dims.sqsize), (self.board_dims.xcor + self.board_dims.size, self.board_dims.ycor + self.board_dims.sqsize), self.linewidth)
        pygame.draw.line(surface, LINE_COLOUR, (self.board_dims.xcor, self.board_dims.ycor + self.board_dims.size - self.board_dims.sqsize), (self.board_dims.xcor + self.board_dims.size, self.board_dims.ycor + self.board_dims.size - self.board_dims.sqsize), self.linewidth)

    def get_row(self, yclick):
        row = yclick // self.board_dims.sqsize
        if row > 2: row %= SQR_SIZE
        return row
    
    def get_column(self, xclick):
        col = xclick // self.board_dims.sqsize
        if col > 2: col %= SQR_SIZE
        return col
    
    def validate_sqr(self, xclick, yclick):
        row = self.get_row(yclick)
        col = self.get_column(xclick)
        sqr = self.squares[row][col]

        # base case
        if not isinstance(sqr, Board):
            # square has to be empty or board not won
            return sqr == 0 and self.active

        # if using ultimate board
        return sqr.validate_sqr(xclick, yclick)
    
    def mark_sqr_plyr_clicked(self, xclick, yclick, player):
        row = self.get_row(yclick)
        col = self.get_column(xclick)
        sqr = self.squares[row][col]

        # base case
        if not isinstance(sqr, Board):
            self.squares[row][col] = player
            return

        # if using ultimate board
        return sqr.mark_sqr_plyr_clicked(xclick, yclick, player)

    def draw_symbol(self, surface, xclick, yclick):
        row = self.get_row(yclick)
        col = self.get_column(xclick) 
        sqr = self.squares[row][col]

        # base case
        if not isinstance(sqr, Board):

            # Cross
            if sqr == 1:
                start_pos_ltr = (self.board_dims.xcor + (col * self.board_dims.sqsize) + self.offset, 
                        self.board_dims.ycor + (row * self.board_dims.sqsize) + self.offset)
                end_pos_ltr = (self.board_dims.xcor + self.board_dims.sqsize * (1 + col) - self.offset, 
                        self.board_dims.ycor + self.board_dims.sqsize * (1 + row) - self.offset)
                pygame.draw.line(surface, CROSS_COLOUR, start_pos_ltr, end_pos_ltr, self.linewidth + 3)

                start_pos_rtl = (self.board_dims.xcor + (col * self.board_dims.sqsize) + self.offset, 
                        self.board_dims.ycor + self.board_dims.sqsize * (1 + row) - self.offset)
                end_pos_rtl = (self.board_dims.xcor + self.board_dims.sqsize * (1 + col) - self.offset, 
                        self.board_dims.ycor + (row * self.board_dims.sqsize) + self.offset)
                pygame.draw.line(surface, CROSS_COLOUR, start_pos_rtl, end_pos_rtl, self.linewidth + 3)

            # Circle
            elif sqr == 2:
                center = (self.board_dims.xcor + self.board_dims.sqsize * (0.5 + col),
                          self.board_dims.ycor + self.board_dims.sqsize * (0.5 + row))
                pygame.draw.circle(surface, (255,0,0), center, self.radius, 5)

            return

        # if using ultimate board
        sqr.draw_symbol(surface, xclick, yclick)

    def check_sqr_win(self, player, xclick, yclick):
        row = self.get_row(yclick)
        col = self.get_column(xclick) 
        sqr = self.squares[row][col]

        # if using ultimate board
        if isinstance(sqr, Board):
            return sqr.check_sqr_win(player, xclick, yclick)

        # checks for vertical lines
        for v in range(SQR_SIZE):
            if self.squares[0][v] == self.squares[1][v] == self.squares[2][v] == player and self.active == True:
                self.active = False
                self.brd_winner = player
                return True
        
        # checks for horizontal lines
        for h in range(SQR_SIZE):
            if self.squares[h][0] == self.squares[h][1] == self.squares[h][2] == player and self.active == True:
                self.active = False
                self.brd_winner = player
                return True

        # checks diagonal lines
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] == player and self.active == True:
            self.active = False
            self.brd_winner = player
            return True

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] == player and self.active == True:
            self.active = False
            self.brd_winner = player
            return True

    def check_brd_win(self, player):
        # used to check if board is ultimate or not
        sqr = self.squares[0][0]
        if not isinstance(sqr, Board):
            if self.active == False:
                return True
            return False
            
        player_wins_brd = [([0] * SQR_SIZE) for row in range(SQR_SIZE)]

        # create a "board" which represents which squares are owned by which player
        for row in range(SQR_SIZE):
            for col in range(SQR_SIZE):
                sqr: Board = self.squares[row][col]
                player_wins_brd[row][col] = sqr.brd_winner

        # checks for vertical lines
        for v in range(SQR_SIZE):
            if player_wins_brd[0][v] == player_wins_brd[1][v] == player_wins_brd[2][v] == player:
                return True

        # checks for horizontal lines
        for h in range(SQR_SIZE):
            if player_wins_brd[h][0] == player_wins_brd[h][1] == player_wins_brd[h][2] == player:
                return True

        # checks diagonal lines
        if player_wins_brd[0][0] == player_wins_brd[1][1] == player_wins_brd[2][2] == player:
            return True

        if player_wins_brd[0][2] == player_wins_brd[1][1] == player_wins_brd[2][0] == player:
            return True
    
    def draw_sqr_symbol(self, surface, xclick, yclick):
        row = self.get_row(yclick)
        col = self.get_column(xclick)
        sqr = self.squares[row][col]

        if isinstance(sqr, Board):
            sqr_win_surface = pygame.Surface((sqr.board_dims.size, sqr.board_dims.size))
            sqr_win_surface.set_alpha(ALPHA)
            if sqr.brd_winner == 1:
                sqr_win_surface.fill(BLUE_WIN)
            else:
                sqr_win_surface.fill(RED_WIN)
            surface.blit(sqr_win_surface, (sqr.board_dims.xcor, sqr.board_dims.ycor))

    def disable_board(self):
        for row in range(SQR_SIZE):
            for col in range(SQR_SIZE):
                sqr: Board = self.squares[row][col]
                sqr.active = False

    def check_for_tie_square(self, xclick, yclick, surface):
        row = self.get_row(yclick)
        col = self.get_column(xclick)
        sqr = self.squares[row][col]

        # base case
        if not isinstance(sqr, Board):
            squares_clicked = 0
            for row in range(SQR_SIZE):
                for col in range(SQR_SIZE):
                    clicked_by = self.squares[row][col]
                    if clicked_by == 1 or clicked_by == 2:
                        squares_clicked += 1

            if squares_clicked == 9 and self.active == True:
                self.tie_sqr = True
                self.active = False
                return True
            else:
                return False

        # if using ultimate board
        return sqr.check_for_tie_square(xclick, yclick, surface)
    
    def draw_tie_square(self, surface, xclick, yclick):
        row = self.get_row(yclick)
        col = self.get_column(xclick)
        sqr = self.squares[row][col]

        if isinstance(sqr, Board):
            sqr_tie_surface = pygame.Surface((sqr.board_dims.size, sqr.board_dims.size))
            sqr_tie_surface.set_alpha(ALPHA)
            sqr_tie_surface.fill(GREY)

            surface.blit(sqr_tie_surface, (sqr.board_dims.xcor, sqr.board_dims.ycor))   
    
    def check_for_tie_game(self):
        sqr = self.squares[0][0]

        # non-ultimate
        if not isinstance(sqr, Board):
            if self.tie_sqr == True:
                return True
        else:
            # ultimate
            main_squares_solved = 0
            for row in range(SQR_SIZE):
                for col in range(SQR_SIZE):
                    sqr: Board = self.squares[row][col]
                    if sqr.active == False:
                        main_squares_solved += 1

            if main_squares_solved == 9:
                return True
