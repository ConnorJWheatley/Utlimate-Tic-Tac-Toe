import pygame
import sys

from constants import *
from game import Game
from button import Button
from tkinter import messagebox

class UltimateTTT:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.ultimate_mode = True
        self.main_menu_bg = pygame.image.load("assets/uttt_bg.png")

    def main_menu(self):
        screen = self.screen
        pygame.display.set_caption("Main Menu")
        play_img = pygame.image.load("assets/PLAY_button.png")
        settings_img = pygame.image.load("assets/SETTINGS_button.png")
        quit_img = pygame.image.load("assets/QUIT_button.png")

        while True:
            self.screen.blit(self.main_menu_bg, (0, 0)) # sets background of start menu

            pygame.font.init()
            game_title_font = pygame.font.SysFont("impact", 110)
            author_font = pygame.font.SysFont("impact", 30)
            game_title = game_title_font.render("ULTIMATE TIC-TAC-TOE", True, WHITE)
            author_name = author_font.render("by Connor Wheatley BSc.", True, WHITE)
            screen.blit(game_title, (130, 50))
            screen.blit(author_name, (775, 180))

            # create buttons
            play_btn = Button(BTN_TOPLEFT, 300, play_img, 0.8)
            settings_btn = Button(BTN_TOPLEFT, 600, settings_img, 0.8)
            quit_btn = Button(BTN_TOPLEFT, 900, quit_img, 0.8)
            play_btn.draw_btn(screen)
            settings_btn.draw_btn(screen)
            quit_btn.draw_btn(screen)

            for event in pygame.event.get():

                if play_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                    self.play()
                if settings_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                    self.settings()
                if quit_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
                
                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def play(self):
        screen = self.screen
        self.game = Game(self.ultimate_mode)
        game = self.game
        pygame.display.set_caption("ULTIMATE TIC TAC TOE")
        game_over = False
        game_over_colour = False
        tie_game = False
        tie_game_colour = False

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

                        # call method to check if a square has been won
                        if game.board.check_sqr_win(game.player, xclick, yclick) == True:
                            
                            # draw shape for whole square
                            game.board.draw_sqr_symbol(screen, xclick, yclick)
                        
                        # check for a tied square
                        if game.board.check_for_tie_square(xclick, yclick, screen):

                            game.board.draw_tie_square(screen, xclick, yclick)
                            
                        # call method to check if board has been won
                        if game.board.check_brd_win(game.player) == True:
                            if self.ultimate_mode == True:
                                game.board.disable_board()
                            game_over = True
                            game_over_colour = True
                        else:
                            if game.board.check_for_tie_game() == True:
                                tie_game = True
                                tie_game_colour = True
                            else:
                                # if game not won, next turn
                                game.next_turn()

                if game_over == True:

                    # Set screen to the colour of the winner
                    while game_over_colour == True:
                        win_surface = pygame.Surface((WIDTH, HEIGHT))
                        win_surface.set_alpha(ALPHA)
                        player_win_font = pygame.font.SysFont("impact", 130)
                        player_win = ""
                        if game.player == 1:
                            player_win = player_win_font.render(f"PLAYER {str(game.player)} HAS WON!", True, WHITE)
                            win_surface.fill(BLUE_WIN)
                        else:
                            player_win = player_win_font.render(f"PLAYER {str(game.player)} HAS WON!", True, WHITE)
                            win_surface.fill(RED_WIN)

                        screen.blit(win_surface, (0, 0))
                        screen.blit(player_win, (110, 220))
                        game_over_colour = False

                    restart_img = pygame.image.load("assets/RESTART_button.png")
                    main_menu_img = pygame.image.load("assets/MAIN_MENU_button.png")

                    restart_btn = Button(BTN_TOPLEFT, 400, restart_img, 0.8)
                    main_menu_btn = Button(BTN_TOPLEFT, 700, main_menu_img, 0.8)

                    restart_btn.draw_btn(screen)
                    main_menu_btn.draw_btn(screen)

                    if restart_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                        self.play()
                    if main_menu_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                        self.main_menu()

                if tie_game == True:

                    while tie_game_colour == True:
                        tie_surface = pygame.Surface((WIDTH, HEIGHT))
                        tie_surface.set_alpha(ALPHA)
                        tie_surface.fill(GREY)
                        tie_font = pygame.font.SysFont("impact", 130)
                        tie_game_text = tie_font.render(f"THIS GAME WAS A TIE!", True, WHITE)

                        screen.blit(tie_surface, (0, 0))
                        screen.blit(tie_game_text, (55, 220))
                        tie_game_colour = False

                    restart_img = pygame.image.load("assets/RESTART_button.png")
                    main_menu_img = pygame.image.load("assets/MAIN_MENU_button.png")

                    restart_btn = Button(BTN_TOPLEFT, 400, restart_img, 0.8)
                    main_menu_btn = Button(BTN_TOPLEFT, 700, main_menu_img, 0.8)

                    restart_btn.draw_btn(screen)
                    main_menu_btn.draw_btn(screen)

                    if restart_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                        self.play()
                    if main_menu_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                        self.main_menu()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def settings(self):
        screen = self.screen
        pygame.display.set_caption("Settings")
        back_img = pygame.image.load("assets/BACK_button.png")
        change_mode_img = pygame.image.load("assets/CHANGE_MODE_button.png")

        while True:
            self.screen.blit(self.main_menu_bg, (0, 0))

            # create buttons
            back_btn = Button(50, 50, back_img, 0.5)
            back_btn.draw_btn(screen)
            change_mode_btn = Button(BTN_TOPLEFT, 200, change_mode_img, 0.8)
            change_mode_btn.draw_btn(screen)

            pygame.font.init()
            ultimate_mode_bool_font = pygame.font.SysFont("impact", 80)
            ultimate_mode_bool = ultimate_mode_bool_font.render("UTTT mode: " + str(self.ultimate_mode), True, WHITE)
            screen.blit(ultimate_mode_bool, (330, 400))

            if back_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                self.main_menu()

            if change_mode_btn.btn_click() and event.type == pygame.MOUSEBUTTONDOWN:
                if self.ultimate_mode == True: 
                    self.ultimate_mode = False
                else: 
                    self.ultimate_mode = True
                messagebox.showinfo("Ultimate mode changed", "You have set ultimate mode to: " + str(self.ultimate_mode))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    ultimateTTT = UltimateTTT()
    ultimateTTT.main_menu()