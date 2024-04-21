class Ship:
    def __init__(self, size, orientation, front_coord):
        """
        Initializes ship object. Sets size/orientation and sets all coordinates in list based on front_coord assuming ship is facing either right or up.
        Arg: size (int): number of cells ship occupies
        Arg: orientation (str): either vertical or horizontal; determines direction ship is facing
        Arg: front_coord (tuple of ints): coordinates of the front of the ship which is facing either right or up
        Return: None
        """
        self.size = size
        self.orientation = orientation
        self.hits = 0
        
        x, y = front_coord
        self.coordinates = [front_coord]
    
        if self.orientation == "horizontal":
            for i in range(1, size):
                self.coordinates.append((x - i, y))
        else:
            for i in range(1, size):
                self.coordinates.append((x, y - i))
    


    def hit(self):
        """
        Adds hit to ship
        Args: None
        Return: None
        """
        self.hits += 1
    
    

    def is_sunk(self):
        """
        Checks if ship is sunk
        Args: None
        Return: Boolean value if ship is sunk
        """
        return self.hits == self.size