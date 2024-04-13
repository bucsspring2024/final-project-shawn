from cell import Cell
from ship import Ship


class Board:
    def __init__(self, size=10):
        """
        Initializes the board object. Creates a list of lists to make a 10x10 board consisting of cells. Creates an empty list for ships.
        Args: size (int): Set to 10; determines the length and width of board
        Return: None
        """
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.ships = []


    def add_ship(self, ship):
        """
        Uses ship coordinates from ship object to add to self.ships list. Sets these coordinates in grid to ship is present.
        Args: ship (object): Takes coordinates from this object to set coordinates in grid to ship is present.
        Return: None
        """
        self.ships.append(ship)
        for coord in ship.coordinates:
            x, y = coord
            self.grid[x][y].place_ship()


    def receive_attack(self, coord):
        """
        Checks to see if attacked coordinate hits a ship and updates the board.
        Args: coord (tuple): Coordiantes in the grid that are being attacked.
        Return: True or False depending on if a ship is hit.
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
        Checks to see if all of the ships are sunk which ends the game.
        Args: None
        Return: True or False depending on if all ships for a player are sunk.
        """
        return all (ship.is_sunk() for ship in self.ships)