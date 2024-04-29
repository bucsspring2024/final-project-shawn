import pygame
from src.controller import Controller
import pygame_menu
from src.ship import Ship
from src.board import Board
from src.player import Player
from src.ai import Ai
from sys import exit


def main():
    pygame.init()
    game = Controller()
    game.mainloop()

main()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
