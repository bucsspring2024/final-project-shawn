from board import Board
from player import Player
from ai import Ai

class Controller:
    def __init__(self):
        self.player_board = Board()
        self.ai_board = Board()
        self.player = Player(self.player_board)
        self.ai = Ai(self.ai_board)
        self.current_turn = "player"


        self.state = "menu"
    

    def mainloop(self):
        while True:
            if self.state == "menu":
                self.menu_loop()
            elif self.state == "game":
                self.game_loop()
            else:
                self.end_loop()
    
    

    def menu_loop(self):
        pass



    def game_loop(self):
        pass

    
    def end_loop(self):
        pass



    def game_setup(self):
        self.set_player_ships()
        self.set_ai_ships()

    
    def play_round(self):
        if self.current_turn == "player":
            coord = self.player.make_move() #Add input from pygame
            hit = self.ai.board.receive_attack(coord)
        else:
            coord = self.ai.make_move()
            hit = self.player.board.receive_attack(coord)
        self.switch_turns()

    def switch_turns(self):
        self.current_turn = "ai" if self.current_turn == "player" else "player"

    def check_game_over(self):
        if self.player.board.all_sunk():
            return True
        elif self.ai.board.all_sunk():
            return True
    
    def set_player_ships(self):
        pass

    def set_ai_ship(self):
        for _ in range(5):
            