from src.ship import Ship


class Board:
    def __init__(self):
        '''
        Initializes the board object by creating list of lists, making a 10x10 board of cell objects. Creates an empty list for ships.
        Args: None
        Return: Nothing
        '''
        self.size = 10
        self.grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []


    def add_ship(self, ship):
        '''
        Appends self.ships list with ship object and assigns corresponding cells to ship
        Arg: ship (object): Takes coordinates from object and assigns corresponding cells to ship
        Return: Nothing
        '''
        self.ships.append(ship)
        for coord in ship.coordinates:
            x, y = coord
            self.grid[x][y].place_ship()


    def receive_attack(self, coord=(0,0)):
        '''
        Checks to see if attacked coordinate hits a ship and updates the board
        Arg: coord (tuple of ints): Coordiantes on the grid being attacked
        Return: (boolean) if ship is hit
        '''
        x, y = coord
        if self.grid[x][y].hit():
            for ship in self.ships:
                if coord in ship.coordinates:
                    ship.hit()
                    return True
        else:
            return False
            
        
    def all_sunk(self):
        '''
        Checks to see if all of the ships are sunk
        Arg: None
        Return: (boolean) if all ships are sunk
        '''
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True
    


class Cell:
    def __init__(self):
        '''
        Initializes cell object that makes up the board. Cell starts as not being hit or assigned ship
        Args: None
        Return: Nothing
        '''
        self.is_ship = False
        self.is_hit = False

    
    def place_ship(self):
        '''
        Used in the add_ship method in Board class to update cell to ship
        Args: None
        Return: Nothing
        '''
        self.is_ship = True

    
    def hit(self):
        '''
        Used in the receive_attack method in Board class. Checks if cell has already been hit and if not, updates cell to hit and checks for ship
        Args: None
        Return: (boolean) if attacked cell is ship and not been hit yet
        '''
        if not self.is_hit:
            self.is_hit = True
            return self.is_ship
        return False