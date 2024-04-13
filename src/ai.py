import random

class AI:
    def __init__(self, board):
        """
        Initializes AI player, setting up their board and all possible moves.
        Args: board (object): the board from Board class that the AI will be attacking.
        Return: None
        """
        self.board = board
        self.possible_moves = [(x, y) for x in range(board.size) for y in range(board.size)]

    
    def make_move(self):
        """
        Randomly picks a cell for the AI to attack.
        Args: None
        Return: move (tuple) coordinates that the AI is attacking.
        """
        move = random.choice(self.possible_moves)
        self.possible_moves.remove(move)
        return move