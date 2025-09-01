import sys

import pygame

from script.utils import load_image, load_images
from script.entitites import PhysicsEntity
from script.tilemap import Tilemap
from script.menu import Menu

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('save obama')
        self.screen = pygame.display.set_mode((1054, 512))
        
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            'caja': load_images('Tiles/caja', (16,16)),
            'piso': load_images('Tiles/pisos', (16,16)),
            'player': load_image('Reptiliano PJ/pjbien.png', (12, 18)), 
            'buttons' : load_images("botones"),
        }

        self.player = PhysicsEntity(self, "player", (50, 50), (8, 16))
        
        self.tilemap = Tilemap(self, tile_size=16)
        
    def run(self):
        while True:

            img = load_image("Obama PJ/Menu chad sin botones.png", (320, 240))
            self.display.blit(img, (0,0))


            self.tilemap.render(self.display)
            self.game_state = "MENU"
            self.menu = Menu(self) 

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()