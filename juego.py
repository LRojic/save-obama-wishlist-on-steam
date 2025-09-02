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
        
        # Estados del juego
        self.game_state = "MENU"  # "MENU", "PLAYING"
        
        # Movimiento del jugador
        self.movement = [False, False]
        
        # Cargar assets
        self.assets = {
            'caja': load_images('Tiles/caja', (16,16)),
            'piso': load_images('Tiles/pisos', (16,16)),
            'player': load_image('Reptiliano PJ/pjbien.png', (12, 18)), 
            'buttons': load_images("botones"),
        }
        
        # Cargar fondo del menú
        try:
            self.menu_bg = load_image("Obama PJ/Menu chad sin botones.png", (320, 240))
        except:
            # Si no encuentra la imagen, crear un fondo de color
            self.menu_bg = pygame.Surface((320, 240))
            self.menu_bg.fill((200, 150, 100))
        
        # Crear entidades del juego
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 16))
        self.tilemap = Tilemap(self, tile_size=16)
        
        # Crear menú
        self.menu = Menu(self)
    
    def start_game(self):
        """Iniciar el juego"""
        self.game_state = "PLAYING"
    
    def back_to_menu(self):
        """Volver al menú"""
        self.game_state = "MENU"
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Manejar eventos según el estado
                if self.game_state == "MENU":
                    self.menu.handle_events(event)
                elif self.game_state == "PLAYING":
                    # Controles del juego
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = True
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = True
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.player.velocity[1] = -3
                        if event.key == pygame.K_ESCAPE:
                            self.back_to_menu()  # Volver al menú con ESC
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = False
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = False
            
            # Renderizar según el estado
            if self.game_state == "MENU":
                self.menu.update()
                self.menu.render(self.display)
            elif self.game_state == "PLAYING":
                # Lógica del juego
                self.display.fill((135, 206, 235))  # Fondo azul cielo
                
                self.tilemap.render(self.display)
                self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
                self.player.render(self.display)
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()