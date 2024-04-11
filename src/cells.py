class Cells:
    def __init__(self, size=10):
        
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range (size)]
        self.ships = []

    def can_place_ship(self, ship, position, orientation):
        
        for i in range (ship.size):
            if orientation == "horizontal":
                if position[1] + i >= self.size or self.grid[position[0]][position[1] + i] != '~':
                    return False
            elif orientation == "vertical":
                if position [0] + i >= self.size or self.grid [position[0] + i][position[1]] != '~':
                    return False
        return True
    
    def place_ship(self, ship, position, orientation):
        