import random

class AI:
    def __init__(self, board):
        self.board = board
        self.possible_moves = [(x, y) for x in range(board.size) for y in range(board.size)]

    def make_move(self):
        move = random.choice(self.possible_moves)
        self.possible_moves.remove(move)
        return move

    def update_possible_moves(self, move):
        if move in self.possible_moves:
            self.possible_moves.remove(move)
