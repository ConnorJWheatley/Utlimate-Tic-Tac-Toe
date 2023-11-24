import pygame
import sys

from constants import *
from game import Game
from button import Button

class UltimateTTT:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game(ultimate_mode=True) # have this be a value that can be configured in a settings menu before starting the game
        self.main_menu_bg = pygame.image.load("assets/uttt_bg.png")

    def main_menu(self):
        screen = self.screen

        pygame.display.set_caption("Main Menu")
        play_img = pygame.image.load("assets/PLAY_button.png")
        settings_img = pygame.image.load("assets/SETTINGS_button.png")
        quit_img = pygame.image.load("assets/QUIT_button.png")

        while True:
            self.screen.blit(self.main_menu_bg, (0, 0)) # sets background of start menu
            BTN_TOPLEFT = (WIDTH / 3 - 50)

            # create buttons
            play_btn = Button(BTN_TOPLEFT, 300, play_img, 0.8)
            settings_btn = Button(BTN_TOPLEFT, 600, settings_img, 0.8)
            quit_btn = Button(BTN_TOPLEFT, 900, quit_img, 0.8)
            play_btn.draw_btn(screen)
            settings_btn.draw_btn(screen)
            quit_btn.draw_btn(screen)

            if play_btn.btn_click():
                print("Play")
                self.play()
            if settings_btn.btn_click():
                print("Settings")
            if quit_btn.btn_click():
                print("Quit")
                pygame.quit()
                sys.exit()

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

                    if game.board.validate_sqr(xclick, yclick):

                        # call method where the square that was clicked in can no longer be clicked again
                        game.board.mark_sqr_plyr_clicked(xclick, yclick, game.player)

                        # call method to draw the symbol in the square that was clicked
                        game.board.draw_symbol(screen, xclick, yclick)

                        check_sqr_win = game.board.check_sqr_win(game.player, xclick, yclick)

                        # call method to check if a square has been won
                        if check_sqr_win == True:
                            print("YOU WON A SQUARE")

                            # draw shape for whole square
                            game.board.draw_sqr_symbol(screen, xclick, yclick)
                            
                        # call method to check if board has been won
                        if game.board.check_brd_win(game.player) == True:
                            print("YOU WIN PLAYER NUMBER " + str(game.player))
                            # pygame.quit()
                            # sys.exit()
                        
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
    ultimateTTT.main_menu()