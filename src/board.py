from cell import Cell
from ship import Ship

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)
        for coord in ship.coordinates:
            x, y = coord
            self.grid[x][y].place_ship()

    def receive_attack(self, coord):
        x, y = coord
        if self.grid[x][y].hit():
            print("Hit!")
            return True
        else:
            print("Miss!")
            return False
    
    def all_sunk(self):
        return all (ship.is_sunk() for ship in self.ships)
    
    def display(self, show_ships = False):
        for row in self.grid:
            for cell in row:
                if cell.is_hit:
                    char = 'X' if cell.is_ship else 'M'
                else:
                    char = 'O' if cell.is_ship and show_ships else '.'
                print(char, end='') 
            print()