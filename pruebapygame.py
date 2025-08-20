import pygame, sys
from script.entitites import PhysicsEntity
from script.utils import load_image

class Game:
    def __init__ (self) :
                
        pygame.init ()
        try: 
            pygame.mixer.init ()
            pygame.mixer.music.load ("fotitos y audio/Audios sigmas/dj-totote producer tag.mp3")
            pygame.mixer.music.play ()
        
        except :
            pass
    
        self.screen = pygame.display.set_mode ((1640, 920))
        self.movement = [False, False]
        self.clock = pygame.time.Clock ()

        pygame.display.set_caption ("Why Always Obama?")

        img = load_image("Reptiliano PJ/reptiliano prime.png")
        width, height = img.get_size ()
        new_size = (width*4,height*4)
        img = pygame.transform.scale (img, new_size)
        self.player = PhysicsEntity(self, "player", (500, 200), (15, 15))
        self.assets = {"player": img,
                       "piso" : load_image('tiles/piso'),
                       "caja" : load_image('tiles/caja'),
                       "silla" : load_image('tiles/silla'),
                       "mesa" : load_image('tiles/mesa'),
                        }
        print (self.assets)

    def run (self) :
        
        while True :
            img = load_image ("DJ Totote Fondo/DJ totote prime.png")
            self.screen.blit(img, (0, 0))
            self.player.update (((self.movement [1] - self.movement [0])*4, 0))
            self.player.render (self.screen)
                
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
            pygame.display.update ()
            self.clock.tick (60)

Game().run ()