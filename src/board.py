from ship import Ship


class Board:
    def __init__(self, size=10):
        """
        Initializes the board object. Creates a list of lists to make a 10x10 board of cell objects and creates an empty list for ships.
        Arg: size (int): Default is 10; the length and width of board
        Return: None
        """
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.ships = []


    def add_ship(self, ship):
        """
        Appends self.ships list with ship object and assigns corresponding cells to ship
        Arg: ship (object): Takes coordinates from object and assigns corresponding cell to ship
        Return: None
        """
        self.ships.append(ship)
        for coordinates in ship.coordinates:
            x, y = coordinates
            self.grid[x][y].place_ship()


    def receive_attack(self, coord):
        """
        Checks to see if attacked coordinate hits a ship and updates the board
        Args coord (tuple): Coordiantes in the grid that are being attacked
        Return: Boolean value depending on if ship is hit
        """
        x, y = coord
        cell = self.grid[x][y]
        if cell.hit():
            for ship in self.ships:
                if coord in ship.coordinates:
                    ship.hit()
            return True
        else:
            return False
            
        
    def all_sunk(self):
        """
        Checks to see if all of the ships are sunk
        Arg: None
        Return: Boolean value depending on if all ships are sunk
        """
        return all (ship.is_sunk() for ship in self.ships)
    


class Cell:
    def __init__(self):
        """
        Initializes the cell object that will make the board. Cell starts as not being hit or assigned a ship
        Args: None
        Return: None
        """
        self.is_ship = False
        self.is_hit = False

    
    def place_ship(self):
        """
        Used in the add_ship method in Board class to update the cell as having a ship
        Args: None
        Return: None
        """
        self.is_ship = True

    
    def hit(self):
        """
        Used in the receive_attack method in Board class. Checks if cell has already been hit and if not, updates cell to hit and checks for ship
        Args: None
        Return: Boolean value depending on if attacked cell has a ship and has not been hit yet
        """
        if not self.is_hit:
            self.is_hit = True
            return self.is_ship
        return False
