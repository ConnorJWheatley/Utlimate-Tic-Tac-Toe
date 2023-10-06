import pygame
import sys

from constants import *
from game import Game

class Main:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ULTIMATE TIC TAC TOE")
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game

        self.screen.fill(BG_COLOUR)
        game.render_board(screen)

        while True:
            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                    xclick, yclick = event.pos

                    if game.board.valid_sqr(xclick, yclick):
                        print("You have clicked in a valid area!")
                        # game.board.mark_sqr(xclick, yclick, game.player)
                        # game.board.draw_fig(screen, xclick, yclick)

                        # # ultimate winner ?
                        # winner = game.board.check_draw_win(screen)
                        # if winner:
                        #     game.board.manage_win(screen, winner, onmain=True)
                        #     game.ultimate_winner(screen, winner)

                        # game.next_turn()
                    else:
                        print("That was not a valid square I am afraid love")

                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()