class Player:
    def __init__(self, board):
        """
        Initializes board the user will be attacking.
        Args: board (object): board from the Board class that the user is attacking.
        Return: None
        """
        self.board = board

    
    def make_move(self, coord):
        """
        Returns the coordinates that the player is attacking
        Args: coord (tuple) coordinates of cell being attacked
        Return: move (tuple) coordinates of cell being attacked
        """
        move = coord
        return move