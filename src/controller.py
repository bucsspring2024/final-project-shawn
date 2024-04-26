import pygame
import pygame_menu
from ship import Ship
from board import Board
from player import Player
from ai import Ai


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        self.state = "MENU"
        self.menu = self.create_menu()  # Create the menu during initialization

    def create_menu(self):
        # Define the menu and its elements here
        menu = pygame_menu.Menu("Start Menu", self.width, self.height, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.label("Welcome to Battleship!", max_char=-1, font_size=20)
        menu.add.button('Play', self.start_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        return menu

    def start_game(self):
        self.state = "GAME"
        # Additional setup before starting the game can be added here

    def mainloop(self):
        while True:
            if self.state == "MENU":
                self.menu.mainloop(self.screen)  # Display the menu
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "GAMEOVER":
                self.gameoverloop()
            else:
                # Handle unexpected states or exit
                break

    def gameloop(self):
        # Game loop logic goes here
        pass

    def gameoverloop(self):
        # Create a simple game over screen
        gameover_menu = pygame_menu.Menu('Game Over', self.width, self.height, theme=pygame_menu.themes.THEME_BLUE)
        
        gameover_menu.add.label("Congratulations, you've completed the game!", max_char=-1, font_size=20)
        gameover_menu.add.button('Play Again', self.restart_game)
        gameover_menu.add.button('Exit', pygame_menu.events.EXIT)

        gameover_menu.mainloop(self.screen)

    def restart_game(self):
        # Reset game state and start over
        self.state = "MENU"
        self.menu = self.create_menu()  # Re-create the menu
        self.menu.mainloop(self.screen)  # Display the menu

# Run the game
if __name__ == '__main__':
    controller = Controller()
    controller.mainloop()