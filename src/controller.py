import pygame
import pygame_menu
from src.ship import Ship
from src.board import Board
from src.player import Player
from src.ai import Ai
from sys import exit


class Controller():
    def __init__(self):
        '''
        Initializes the controller object. Sets up menus and display elements that are not going to be changing.
        Args: None
        Return: Nothing
        '''
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen.fill("lightblue")
        self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption("Battleship")
        self.state = "MENU"
        self.current_turn = "player"



        self.font = pygame.font.Font(None, 75)
        self.background = pygame.image.load("./assets/background.jpg")
        self.title_surface = self.font.render("Battleship", False, "Black")
        self.player_surface = self.font.render("Player", False, "Black")
        self.opponent_surface = self.font.render("Opponent", False, "Black")
    
        

        self.menu = pygame_menu.Menu("Start Menu", self.width, self.height, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.menu.add.label("Welcome to Battleship!", max_char = -1, font_size = 20)
        self.menu.add.button("Play", self.start_game)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        self.menu.add.button("High Score", self.start_high_score_menu_screen)

        self.win_menu = pygame_menu.Menu("Game Over", self.width, self.height, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.win_menu.add.label("Congatulations, You Won", max_char = -1, font_size = 20)
        self.win_menu.add.button("Play Again", self.start_game)
        self.win_menu.add.button("Quit", pygame_menu.events.EXIT)

        self.lose_menu = pygame_menu.Menu("Game Over", self.width, self.height, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.lose_menu.add.label("You Lost, Better Luck Next Time", max_char = -1, font_size = 20)
        self.lose_menu.add.button("Play Again", self.start_game)
        self.lose_menu.add.button("Quit", pygame_menu.events.EXIT)


        self.high_score_file = open("./assets/high_score.txt", "r")
        self.high_score = self.high_score_file.read()
        self.high_score_file.close()
    
        self.high_score_menu = pygame_menu.Menu("High Score", self.width, self.height, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.high_score_menu.add.label(f"Current High Score: {self.high_score} moves ", max_char = -1, font_size = 20)
        self.high_score_menu.add.button("Play Again", self.start_game)
        self.high_score_menu.add.button("Quit", pygame_menu.events.EXIT)




    def menuloop(self):
        '''
        Draws and updates menu screen
        Args: None
        Return: Nothing
        '''
        while self.state == "MENU":
            if self.menu.is_enabled():
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                self.menu.update(events)
                self.menu.draw(self.screen)
            pygame.display.flip()
    

    def start_game(self):
        '''
        Used in the menus to start the game
        Args: None
        Return: Nothing
        '''
        self.state = "GAME"



    def winloop(self):
        '''
        Draws and updates the menu after winning a game
        Args: None
        Return: Nothing
        '''
        while self.state == "WIN":
            if self.win_menu.is_enabled():
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                self.win_menu.update(events)
                self.win_menu.draw(self.screen)
            pygame.display.flip()

    def loseloop(self):
        '''
        Draws and updates the menu after losing a game
        Args: None
        Return: Nothing
        '''
        while self.state == "LOSE":
            if self.lose_menu.is_enabled():
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                self.lose_menu.update(events)
                self.lose_menu.draw(self.screen)
            pygame.display.flip()



    def high_score_loop(self):
        '''
        Draws and updates the menu screen for viewing the current high score
        Args: None
        Return: Nothing
        '''
        while self.state == "HIGHSCORE":
            if self.high_score_menu.is_enabled():
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                self.high_score_menu.update(events)
                self.high_score_menu.draw(self.screen)
            pygame.display.flip()

    def start_high_score_menu_screen(self):
        '''
        Used in the starting menu to switch the screen to high score menu
        Args: None
        Return: Nothing
        '''
        self.state = "HIGHSCORE"




    def gameloop(self):
        '''
        Sets up gameloop needed for gameplay. Draws and updates background, grid and places ship images that depend on grid. Checks for user events and contains game logic to update screen and progress game forward. Keeps track of number of moves and updates high score if broken.
        Args: None
        Return: Nothing
        '''
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.title_surface, (self.width/2.5 + 25, self.height/12))
        self.screen.blit(self.player_surface, (self.width/1.4, self.height/1.08))
        self.screen.blit(self.opponent_surface, (self.width/5.8, self.height/1.08))

        grid_size = 10
        cell_size = 60
        grid_margin = 75

        player_cells = []
        ai_cells = []

        for row in range(grid_size):
            for col in range(grid_size):
                x = col * cell_size + grid_margin
                y = row * cell_size + grid_margin + 120
                pygame.draw.rect(self.screen, "black" , (x, y, cell_size, cell_size), 1)
                ai_cells.append(pygame.Rect(x, y, cell_size, cell_size)) 

        ai_grid_offset = grid_margin + grid_size * cell_size + 175
        for row in range(grid_size):
            row_cells = [] 
            for col in range(grid_size):
                x = col * cell_size + ai_grid_offset
                y = row * cell_size + grid_margin + 120
                pygame.draw.rect(self.screen, "black", (x, y, cell_size, cell_size), 1)
                row_cells.append(pygame.Rect(x, y, cell_size, cell_size))
            player_cells.append(row_cells)



        carrier  = pygame.image.load("./assets/carrier.jpg")
        battleship  = pygame.image.load("./assets/battleship.jpg")
        cruiser  = pygame.image.load("./assets/cruiser.jpg")
        destroyer = pygame.image.load("./assets/destroyer.jpg")
        submarine  = pygame.image.load("./assets/submarine.jpg")

        carrier = pygame.transform.scale(carrier, (5 * cell_size, cell_size))
        carrier = pygame.transform.rotate(carrier, 90)
        battleship = pygame.transform.scale(battleship, (4 * cell_size, cell_size))
        destroyer = pygame.transform.scale(destroyer, (3 * cell_size, cell_size))
        destroyer = pygame.transform.rotate(destroyer, 90)
        cruiser = pygame.transform.scale(cruiser, (3 * cell_size, cell_size))
        submarine = pygame.transform.scale(submarine, (2 * cell_size, cell_size))
        submarine = pygame.transform.rotate(submarine, 90)

        self.screen.blit(carrier, (8 * cell_size + ai_grid_offset, 1 * cell_size + grid_margin + 120))
        self.screen.blit(battleship, (2 * cell_size + ai_grid_offset, 9 * cell_size + grid_margin + 120))
        self.screen.blit(destroyer, (1 * cell_size + ai_grid_offset, 1 * cell_size + grid_margin + 120))
        self.screen.blit(cruiser, (4 * cell_size + ai_grid_offset, 0 * cell_size + grid_margin + 120))
        self.screen.blit(submarine, (5 * cell_size + ai_grid_offset, 6 * cell_size + grid_margin + 120))



        carrier_size = 5
        battleship_size = 4
        destroyer_size = 3
        cruiser_size = 3
        submarine_size = 2
        carrier_coord = ((8,1), (8,2), (8,3), (8,4), (8,5))
        battleship_coord = ((2,9), (3,9), (4,9), (5,9))
        destroyer_coord = ((1,1), (1,2), (1,3),)
        cruiser_coord = ((4,0), (5,0), (6,0))
        submarine_coord = ((5,6), (5,7))
        
        player_carrier = Ship(carrier_size, carrier_coord)
        player_battleship = Ship(battleship_size, battleship_coord)
        player_destroyer = Ship(destroyer_size, destroyer_coord)
        player_cruiser = Ship(cruiser_size, cruiser_coord)
        player_submarine = Ship(submarine_size, submarine_coord)
        player_ships = [player_carrier, player_battleship, player_destroyer, player_submarine, player_cruiser]

        ai_carrier = Ship(carrier_size, carrier_coord)
        ai_battleship = Ship(battleship_size, battleship_coord)
        ai_destroyer = Ship(destroyer_size, destroyer_coord)
        ai_cruiser = Ship(cruiser_size, cruiser_coord)
        ai_submarine = Ship(submarine_size, submarine_coord)
        ai_ships = [ai_carrier, ai_battleship, ai_destroyer, ai_submarine, ai_cruiser]

        player_board = Board()
        ai_board = Board()
        
        for ship in player_ships:
            player_board.add_ship(ship)
        
        for ship in ai_ships:
            ai_board.add_ship(ship)

        player = Player(player_board)
        ai = Ai(ai_board)



        number_of_moves = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif self.current_turn == "player":
                   if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos_x, mpos_y = event.pos
                    row = (mpos_y - grid_margin - 120) // cell_size
                    col = (mpos_x - grid_margin) // cell_size
                    for cell in ai_cells:
                            if cell.collidepoint(mpos_x, mpos_y):
                                player_move = player.make_move((row, col))
                                if ai_board.receive_attack(player_move) == True:
                                    self.current_turn = "ai"
                                    pygame.draw.rect(self.screen, "green", cell)
                                    number_of_moves += 1
                                elif ai_board.receive_attack(player_move)==False:
                                    self.current_turn = "ai"
                                    pygame.draw.rect(self.screen, "red", cell)
                                    number_of_moves += 1
                                    
                elif self.current_turn == "ai":
                    pygame.time.wait(2000)
                    ai_move = ai.make_move()
                    ai_col, ai_row = ai_move
                    if player_board.receive_attack(ai_move) == True:
                        pygame.draw.rect(self.screen, "green", player_cells[ai_row][ai_col])
                        self.current_turn = "player"
                    elif player_board.receive_attack(ai_move) == False:
                        pygame.draw.rect(self.screen, "red", player_cells[ai_row][ai_col])
                        self.current_turn = "player"

            if player_board.all_sunk():
                running = False
                self.state = "LOSE"
                self.current_turn = "player"
            elif ai_board.all_sunk():
                running = False
                self.state = "WIN"
                self.current_turn = "player"

            pygame.display.flip()


        high_score_file = open("./assets/high_score.txt", "r")
        high_score = high_score_file.read()
        high_score_file.close()
        high_score = int(high_score)

        if number_of_moves < high_score:
            high_score_file = open("./assets/high_score.txt", "w")
            high_score_file.write(str(number_of_moves))
            high_score_file.close()




    def mainloop(self):
        '''
        Determines state of the game; whether its in gameplay or in a menu
        Args: None
        Return: Nothing
        '''
        while True:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "WIN":
                self.winloop()
            elif self.state == "LOSE":
                self.loseloop()
            elif self.state == "HIGHSCORE":
                self.high_score_loop()