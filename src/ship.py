class Ship:
    def __init__(self, size, coordinates, orientation="vertical"):
        """
        Initializes the ship object. Sets the size, coordinates and orientation of the ship, while starting the ship's hits at zero.
        Arg: size (int): the number of cells the ship occupies
        Arg: coordinates (list of tuples): the coordinates of the cells that the ship occupies
        Arg: orientation (str): either vertical or horizontal; sets orientation of ship
        Return: None
        """
        self.size = size
        self.coordinates = coordinates
        self.orientation = orientation
        self.hits = 0

    
    def is_sunk(self):
        """
        Checks if the ship is sunk
        Args: None
        Return: Boolean value representing if ship is sunk
        """
        return self.hits == self.size

    
    def hit(self):
        """
        Adds 1 to the ship's hits
        Args: None
        Return: None
        """
        self.hits += 1