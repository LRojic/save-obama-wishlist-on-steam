import pygame, sys
from time import sleep
from script.entitites import PhysicsEntity
from script.utils import load_image, load_images
from script.tilemap import Tilemap

class Game:
    def __init__ (self) :
                
        pygame.init ()

        try :
            pygame.mixer.init ()
            pygame.mixer.music.load ("img/Audios Sigmas/dj-totote producer tag.mp3")
            pygame.mixer.music.play ()
            sleep (2.5)
        except :
            pass

            
        pygame.display.set_caption ("Why Always Obama?")
        self.display = pygame.Surface ((320, 240))
        self.screen = pygame.display.set_mode ((1640, 920))
        self.movement = [False, False]
        self.clock = pygame.time.Clock ()
        
        self.assets = {"piso" : load_images('Tiles/pisos'),
                       "caja" : load_images('Tiles/caja'),
                       "silla" : load_image('Tiles/silla/banquitobama.png'),
                       "player": load_image("Reptiliano PJ/reptiliano prime.png"),
                        }
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))
        self.tilemap = Tilemap(self,  tile_size=16)       

    def run (self) :
        try :
            pygame.mixer.init ()
            pygame.mixer.music.load ("img/Audios Sigmas/obama have dihh hoodtrap song.mp3")
            pygame.mixer.music.set_volume(0.4)  
            pygame.mixer.music.play (-1)
        except :
            pass
        
        while True :
            self.display.fill((255,255,255))

            self.tilemap.render(self.display)

            self.player.update (self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render (self.display)
            print(self.tilemap.physics_rects_around(self.player.pos))
                
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