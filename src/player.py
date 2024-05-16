class Player:
    def __init__(self, board):
        '''
        Initializes the user's board
        Arg: board (object): board from the Board class
        Return: Nothing
        '''
        self.board = board

    
    def make_move(self, coord=(0,0)):
        '''
        Returns the coordinates that the player is attacking
        Args: coord (tuple of ints) coordinates of cell being attacked
        Return: coord (tuple of ints) coordinates of cell being attacked
        '''
        return coord