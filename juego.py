import sys
import pygame
from script.utils import load_image, load_images
from script.entitites import PhysicsEntity
from script.tilemap import Tilemap
from script.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Save Obama')
        self.screen = pygame.display.set_mode((1054, 512))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        
        # estado del juego
        self.game_state = "MENU"  # menu playing
        
        # movimiento del jugador
        self.movement = [False, False]
        
        # cargar assets
        self.assets = {
            'caja': load_images('Tiles/caja', (16,16)),
            'piso': load_images('Tiles/pisos', (16,16)),
            'player': load_image('Reptiliano PJ/pjbien.png', (12, 18)), 
            'buttons': load_images("botones"),
        }
        
        # cargar fondo del menú

        self.menu_bg = load_image("Obama_PJ/Menu_chad_sin_botones.png", (320, 240))
        
        # crear entidades del juego
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 16))
        self.tilemap = Tilemap(self, tile_size=16)
        
        # crear menú
        self.menu = Menu(self)
    
    def start_game(self):
        # inicia el juego
        self.game_state = "PLAYING"
    
    def back_to_menu(self):
        # volver al menú
        self.game_state = "MENU"
    
    def run(self):
        # arranque
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() # para salir
                
                # maneja eventos según el estado
                if self.game_state == "MENU":
                    self.menu.handle_events(event)
                elif self.game_state == "PLAYING":
                    # controles del juego
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = True
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = True
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.player.velocity[1] = -3
                        if event.key == pygame.K_ESCAPE:
                            self.back_to_menu()  # volver al menú con ESC
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = False
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = False
            
            # renderizar segun el estado
            if self.game_state == "MENU":
                self.menu.update()
                self.menu.render(self.display)
            elif self.game_state == "PLAYING":
                # render de lo que se muestra
                self.display.fill((135, 206, 235))  # fondo azul cielo
                
                self.tilemap.render(self.display)
                self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
                self.player.render(self.display)
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)) # escalar a pantalla
            pygame.display.update()
            self.clock.tick(60)

Game().run()