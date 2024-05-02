import random


class Ai:
    def __init__(self, board):
        '''
        Initializes Ai and sets up their board and all possible moves
        Arg: board (object): board from the Board class
        Return: Nothing
        '''
        self.board = board
        self.possible_moves = [(x, y) for x in range(board.size) for y in range(board.size)]


    def make_move(self):
        '''
        Randomly picks a cell for the Ai to attack
        Args: None
        Return: move (tuple): coordinates that the Ai is attacking
        '''
        move = random.choice(self.possible_moves)
        self.possible_moves.remove(move)
        return move