import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        # Movimiento horizontal
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:  # Moviendo a la derecha
                    self.pos[0] = rect.left - self.size[0]
                    self.collisions['right'] = True
                if frame_movement[0] < 0:  # Moviendo a la izquierda
                    self.pos[0] = rect.right
                    self.collisions['left'] = True
                # Resetear velocidad horizontal si choca
                self.velocity[0] = 0
        
        # Movimiento vertical
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:  # Cayendo
                    self.pos[1] = rect.top - self.size[1]
                    self.collisions['down'] = True
                if frame_movement[1] < 0:  # Saltando
                    self.pos[1] = rect.bottom
                    self.collisions['up'] = True
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)