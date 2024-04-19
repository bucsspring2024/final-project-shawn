from player import Player
from ai import Ai
from board import Board




class Controller:
    def __init__(self, player, ai):
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