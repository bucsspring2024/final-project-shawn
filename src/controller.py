import pygame
import pygame_menu
from ship import Ship
from board import Board
from player import Player
from ai import Ai
from sys import exit


class Controller():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen.fill("lightblue")
        self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption("Battleship")
        self.state = "MENU"

        self.font = pygame.font.Font(None, 75)
        self.font2 = pygame.font.Font(None, 35)
        self.background = pygame.image.load("../assets/background.jpg")
        self.current_turn = "player"

        self.menu = pygame_menu.Menu("Start Menu", self.width, self.height, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.label("Welcome to Battleship!", max_char = -1, font_size = 20)
        self.menu.add.button("Play", self.start_game)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

    def background_setup(self):
        title_surface = self.font.render("Battleship", False, "Black")
        player_surface = self.font.render("Player", False, "Black")
        opponent_surface = self.font.render("Opponent", False, "Black")
    
        self.screen.blit(self.background, (0,0))
        self.screen.blit(title_surface, (self.width/2.5 + 25, self.height/12))
        self.screen.blit(player_surface, (self.width/1.4, self.height/1.08))
        self.screen.blit(opponent_surface, (self.width/5.8, self.height/1.08))

    

    def gameloop(self):
        self.background_setup()

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

        carrier  = pygame.image.load("../assets/carrier.jpg")
        battleship  = pygame.image.load("../assets/battleship.jpg")
        cruiser  = pygame.image.load("../assets/cruiser.jpg")
        destroyer = pygame.image.load("../assets/destroyer.jpg")
        submarine  = pygame.image.load("../assets/submarine.jpg")

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

        
        carrier = Ship(5, ((8,1), (8,2), (8,3), (8,4), (8,5)))
        battleship = Ship(4, ((2,9), (3,9), (4,9), (5,9)))
        destroyer = Ship(3, ((1,1), (1,2), (1,3),))
        submarine = Ship(3, ((4,0), (5,0), (6,0)))
        cruiser = Ship(2, ((5,6), (5,7)))
        ships = [carrier, battleship, destroyer, submarine, cruiser]

        ai_carrier = Ship(5, ((8,1), (8,2), (8,3), (8,4), (8,5)))
        ai_battleship = Ship(4, ((2,9), (3,9), (4,9), (5,9)))
        ai_destroyer = Ship(3, ((1,1), (1,2), (1,3),))
        ai_submarine = Ship(3, ((4,0), (5,0), (6,0)))
        ai_cruiser = Ship(2, ((5,6), (5,7)))
        ai_ships = [ai_carrier, ai_battleship, ai_destroyer, ai_submarine, ai_cruiser]

        player_board = Board()
        ai_board = Board()
        
        for ship in ships:
            player_board.add_ship(ship)
        
        for ship in ai_ships:
            ai_board.add_ship(ship)

        player = Player(player_board)
        ai = Ai(ai_board)

        player_turn_surface = self.font2.render("Your Turn: Shoot any Cell on the Grid", False, "Black")
        player_hit_surface = self.font2.render("Hit", False, "Black")
        player_miss_surface = self.font2.render("Miss", False, "Black")
        player_battleship_sunk_surface = self.font2.render("Battleship Sunk", False, "Black") 

        ai_turn_surface = self.font2.render("Computer's Turn", False, "Black")
        ai_hit_surface = self.font2.render("Hit", False, "Black")
        ai_miss_surface = self.font2.render("Miss", False, "Black")
        ai_battleship_sunk_surface = self.font2.render("Your Battleship has been sunk", False, "Black")

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
                                    number_of_moves +=1
                                    
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
            elif ai_board.all_sunk():
                running = False
                self.state = "WIN"



            pygame.display.flip()

    def mainloop(self):
        while True:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "WIN":
                self.winloop()
            elif self.state == "LOSE":
                self.loseloop()
            


    def menuloop(self):
            self.menu.mainloop(self.screen)
            pygame.display.flip()


    def start_game(self):
        self.state = "GAME"

      

controller = Controller()
controller.gameloop()