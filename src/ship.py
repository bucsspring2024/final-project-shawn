class Ship:
    def __init__(self, size=3, coordinates=((0,0),(0,1),(0,2))):
        '''
        Initializes ship object. Sets size and coordinates, starts hits at 0.
        Arg: size (int): number of cells ship occupies
        Arg: coordinates (list of tuples): coordinates of the ship
        Return: Nothing
        '''
        self.size = size
        self.coordinates = coordinates
        self.hits = 0
    

    def hit(self):
        '''
        Adds hit to ship
        Args: None
        Return: Nothing
        '''
        self.hits += 1
    
    
    def is_sunk(self):
        '''
        Checks if ship is sunk
        Args: None
        Return: (boolean) if ship is sunk
        '''
        return self.hits == self.size