class Player:
    def __init__(self, board):
        """
        Initializes board the user's board
        Arg: board (object): board from the Board class
        Return: None
        """
        self.board = board

    
    def make_move(self, coord):
        """
        Returns the coordinates that the player is attacking
        Args: coord (tuple) coordinates of cell being attacked
        Return: coord (tuple) coordinates of cell being attacked
        """
        return coord