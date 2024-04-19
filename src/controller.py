import pygame
import pygame_menu
import pygame_gui
from player import Player
from ai import Ai
from board import Board




class Controller:
    def __init__(self, player, ai):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.fill((150, 150, 250))

        width, height = pygame.display.get_window_size()
        self.menu = pygame_menu.Menu("button example", width-20, height/2, position = (10,10))
        self.menu.add.label("Press for a Hero", max_char = -1, font_size = 14)

        self.menu.add.button(
            'Press Me', 
            self.start_game, 
            align=pygame_menu.locals.ALIGN_CENTER
        )
        
        self.button = Button(
            x=50,
            y=self.menu.get_rect().bottom + 10
        )

        self.player = player
        self.ai = ai
        self.current_turn = "player"

    
    def set_player_ships(self):
        pass

    def set_ai_ships(self):
        pass


    def switch_turns(self):
        self.current_turn = "ai" if self.current_turn == "player" else "player"

    
    def play_round(self):
        if self.current_turn == "player":
            coord = self.player.make_move()
            hit = self.ai.board.receive_attack(coord)
        else:
            coord = self.ai.make_move()
            hit = self.player.board.receive_attack(coord)
        self.switch_turns()

    
    def get_player_input(self):
        pass

    def check_game_over(self):
        if self.player.board.all_sunk():
            return True
        elif self.ai.board.all_sunk():
            return True
        

    def start_game(self):
        game_over = False
        while not game_over:
            self.play_round()
            game_over = self.check_game_over()