class Cell:
    def __init__(self):
        self.is_ship = False
        self.is_hit = False

    def place_ship(self):
        self.is_ship = True

    def hit(self):
        if not self.is_hit:
            self.is_hit = True
            return self.is_ship
        return False
