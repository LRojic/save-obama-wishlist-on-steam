import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0] 
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False} # colisiones en cada direccion
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) # funcion para hacer mas rapido
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # aplicar movimiento en pixeles
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect() # el rect de la entidad
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
                # movimiento hasta q detecte una colision q lo frene en el eje x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        # lo mismo pero en y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        # gravedad
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0 
        # si se choca con el piso o el techo se frena la velocidad en y
        
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos) # dibuja la imagen del jugador en la posicion actual
