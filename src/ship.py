class Ship:
    def __init__(self, size, coordinates):
        """
        Initializes the ship object. Sets the size and coordinates of the ship, while starting at zero hits.
        Args: size (int): the number of cells the ship occupies.
        Args: coordinates (list of tuples): the coordinates of the cells that the ship occupies.
        Return: None
        """
        self.size = size
        self.coordinates = coordinates
        self.hits = 0

    
    def is_sunk(self):
        """
        Checks if the ship is sunk.
        Args: None
        Return: True or False depending on if ship is sunk.
        """
        return self.hits == self.size

    
    def hit(self):
        """
        Adds a hit to the ship object
        Args: None
        Return: None
        """
        self.hits += 1