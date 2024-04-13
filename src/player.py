from board import Board

class Player:
    def __init__(self, board):
        self.board = board

    def make_move(self, coord):
        return self.board.receive_attack(coord)