class Cell:
    def __init__(self):
        """
        Initializes the cell object that will make the board. Each cell starts as not having a ship or being hit.
        Args: None
        Return: None
        """
        self.is_ship = False
        self.is_hit = False

    
    def place_ship(self):
        """
        Used in the add_ship method in Board class. Updates the cell so a ship is present.
        Args: None
        Return: None
        """
        self.is_ship = True

    
    def hit(self):
        """
        Used in the receive_attack method in Board class. First checks if the cell has already been hit and if not, updates it to hit and checks if ship is present.
        Args: None
        Return: True or False depending on if a cell that has a ship and has not been hit yet, is hit.
        """
        if not self.is_hit:
            self.is_hit = True
            return self.is_ship
        return False
