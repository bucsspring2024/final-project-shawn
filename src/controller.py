from board import Board
from player import Player
from ai import Ai
from ship import Ship


class Controller:
    def __init__(self):
        self.player_board = Board()
        self.ai_board = Board()
        self.player = Player(self.player_board)
        self.ai = Ai(self.ai_board)
        self.current_turn = "player"
        
        carrier_coord  = (5,1)
        self.player_carrier = Ship(5, carrier_coord)
        self.ai_carrier = Ship(5, carrier_coord)

        battleship_coord  = (4,2)
        self.player_battleship = Ship(4, battleship_coord)
        self.ai_battleship = Ship(4, battleship_coord)

        cruiser_coord  = (3,3)
        self.player_cruiser = Ship(3, cruiser_coord)
        self.ai_cruiser = Ship(3, cruiser_coord)

        submarine_coord  = (3,4)
        self.player_submarine = Ship(3, submarine_coord)
        self.ai_submarine = Ship(3, submarine_coord)

        destroyer_coord  = (2,5)
        self.player_destroyer = Ship(2, destroyer_coord)
        self.ai_destroyer = Ship(2, destroyer_coord)


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
        self.game_setup()
        while not self.check_game_over:
            self.play_round()
        print("game over")

    
    def end_loop(self):
        pass



    def game_setup(self):
        self.set_player_ships()
        self.set_ai_ships()

    
    def play_round(self):
        if self.current_turn == "player":
            coord = self.ai.make_move()
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
        else:
            return False
    
    def set_player_ships(self):
        self.player_board.add_ship(self.player_carrier)
        self.player_board.add_ship(self.player_destroyer)
        self.player_board.add_ship(self.player_submarine)
        self.player_board.add_ship(self.player_battleship)
        self.player_board.add_ship(self.player_cruiser)



    def set_ai_ships(self):
        self.ai_board.add_ship(self.ai_carrier)
        self.ai_board.add_ship(self.ai_destroyer)
        self.ai_board.add_ship(self.ai_submarine)
        self.ai_board.add_ship(self.ai_cruiser)
        self.ai_board.add_ship(self.ai_battleship)




game = Controller()
game.game_loop()