from ship import Ship


class Board:
    def __init__(self):
        """
        Initializes the board object by creating list of lists, making a 10x10 board of cell objects. Creates an empty list for ships.
        Args: None
        Return: None
        """
        self.size = 10
        self.grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []


    def add_ship(self, ship):
        """
        Appends self.ships list with ship object and assigns corresponding cells to ship
        Arg: ship (object): Takes coordinates from object and assigns corresponding cells to ship
        Return: None
        """
        self.ships.append(ship)
        for coord in ship.coordinates:
            x, y = coord
            self.grid[x][y].place_ship()


    def receive_attack(self, coord):
        """
        Checks to see if attacked coordinate hits a ship and updates the board
        Arg: coord (tuple): Coordiantes on the grid being attacked
        Return: Boolean value if ship is hit
        """
        x, y = coord
        hit = self.grid[x][y].hit()
        if hit == True:
            for ship in self.ships:
                if coord in ship.coordinates:
                    ship.hit()
                    print("Hit")
                    return True
                if ship.is_sunk() == True:
                    print("You sunk my battleship")
        else:
            print("Miss")
            return False
            
        
    def all_sunk(self):
        """
        Checks to see if all of the ships are sunk
        Arg: None
        Return: Boolean value if all ships are sunk
        """
        if all (ship.is_sunk() for ship in self.ships) == True:
            return True
        else:
            return False
    


class Cell:
    def __init__(self):
        """
        Initializes the cell object that makes up the board. Cell starts as not being hit or assigned ship
        Args: None
        Return: None
        """
        self.is_ship = False
        self.is_hit = False

    
    def place_ship(self):
        """
        Used in the add_ship method in Board class to update cell to ship
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
