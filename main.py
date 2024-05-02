import pygame
from src.controller import Controller

def main():
    pygame.init()
    battleship = Controller()
    battleship.mainloop()

main()

if __name__ == '__main__':
    main()