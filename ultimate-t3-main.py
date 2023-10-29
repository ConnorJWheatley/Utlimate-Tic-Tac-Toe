import pygame
import sys

from constants import *
from game import Game

class UltimateTTT:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game(ultimate_mode=True) # have this be a value that can be configured in a settings menu before starting the game
        self.main_menu_bg = pygame.image.load("assets/uttt_bg.png")

    def main_menu(self):
        pygame.display.set_caption("Main Menu")
        while True:
            self.screen.blit(self.main_menu_bg, (0, 0))

            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def play(self):
        screen = self.screen
        game = self.game

        screen.fill("black")
        pygame.display.set_caption("ULTIMATE TIC TAC TOE")
        self.screen.fill(BG_COLOUR)
        game.render_board(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                    xclick, yclick = event.pos

                    #
                    if game.board.validate_sqr(xclick, yclick):

                        # call method where the square that was clicked in can no longer be clicked again
                        game.board.mark_sqr_plyr_clicked(xclick, yclick, game.player)

                        # call method to draw the symbol in the square that was clicked
                        game.board.draw_symbol(screen, xclick, yclick)

                        # call method to check if a square has been won
                        game.board.check_sqr_win(game.player)

                        # call method to check if board has been won
                        if game.board.check_brd_win(game.player) == True:
                            pygame.quit()
                            sys.exit()
                        
                        # if game not won, next turn
                        game.next_turn()

                        # make it so cursor changes for squares you aren't allowed to play in

                    else:
                        pass
                        #print("That was not a valid square I am afraid love")

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    ultimateTTT = UltimateTTT()
    ultimateTTT.play()