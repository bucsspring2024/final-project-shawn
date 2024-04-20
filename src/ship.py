class Ship:
    def __init__(self, size, front_coord, orientation="horizontal"):
        """
        Initializes the ship object. Sets the coordinates of the ship using it's orientation and size, assuming it is always facing up or right. Starts hits at 0
        Arg: size (int): the number of cells the ship occupies
        Arg: front_coord (tuple): the coordinates of the front of the ship which is facing right or up
        Arg: orientation (str): either vertical or horizontal; sets orientation of ship
        Return: None
        """
        self.size = size
        self.orientation = orientation
        self.hits = 0
        
        self.coordinates = [front_coord]
        x, y = front_coord
    
        if self.orientation == "horizontal":
            for i in range(size - 1):
                self.coordinates.append((x - i, y))
        else:
            for i in range(size -1):
                self.coordinates.append((x, y - i))
    
    
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