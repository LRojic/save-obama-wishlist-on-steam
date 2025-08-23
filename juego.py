import pygame, sys
from time import sleep
from script.entitites import PhysicsEntity
from script.utils import load_image, load_images
from script.tilemap import Tilemap

class Game:
    def __init__ (self) :
                
        pygame.init ()
        try: 
            pygame.mixer.init ()
            pygame.mixer.music.load ("img/Audios Sigmas/dj-totote producer tag.mp3")
            pygame.mixer.music.set_volume(1) 
            pygame.mixer.music.play ()
            sleep (2.5)

        
        except :
            pass
            
        pygame.display.set_caption ("Why Always Obama?")
        self.display = pygame.Surface ((320, 240))
        self.screen = pygame.display.set_mode ((1640, 920))
        self.movement = [False, False]
        self.clock = pygame.time.Clock ()


        self.player = PhysicsEntity(self, "player", (500, 200), (15, 15))
        self.assets = {"player": load_images("Reptiliano PJ"),
                       "piso" : load_images('Tiles/pisos'),
                       "caja" : load_images('Tiles/caja'),
                       "silla" : load_images('Tiles/silla'),
                        }

        self.tilemap = Tilemap(self,  tile_size=16)       

    def run (self) :
        pygame.mixer.init ()
        pygame.mixer.music.load ("img/Audios Sigmas/obama have dihh hoodtrap song.mp3")
        pygame.mixer.music.set_volume(0.4)  
        pygame.mixer.music.play (-1)

        while True :



            img = load_image ("DJ Totote Fondo/DJ totote prime.png")
            self.screen.blit(img, (0, 0))
            self.player.update (((self.movement [1] - self.movement [0])*4, 0))
            self.player.render (self.display)
            self.tilemap.render(self.display)

                
            for event in pygame.event.get () :
                if event.type == pygame.QUIT :
                    pygame.quit ()
                    sys.exit ()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT :
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT :
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT :
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT :
                        self.movement[1] = False
                #flechas arriba, wasd abajo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a :
                        self.movement[0] = True
                    if event.key == pygame.K_d :
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a :
                        self.movement[0] = False
                    if event.key == pygame.K_d :
                        self.movement[1] = False
            self.screen.blit (pygame.transform.scale(self.display, self.screen.get_size ()), (0, 0))
            pygame.display.update ()
            self.clock.tick (60)

            
Game().run ()