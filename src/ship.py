class Ship:
    def __init__(self, name, size, coordinates):
        self.name = name
        self.size = size
        self.coordinates = coordinates
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.size

    def hit(self):
        self.hits += 1