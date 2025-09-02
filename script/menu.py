import pygame
from script.utils import load_image

class Button:
    def __init__(self, x, y, normal_sprite, hover_sprite, action=None):
        self.x = x
        self.y = y
        self.normal_sprite = normal_sprite
        self.hover_sprite = hover_sprite
        self.action = action
        self.is_hovered = False
        self.rect = pygame.Rect(x, y, normal_sprite.get_width(), normal_sprite.get_height())
    
    def update(self, mouse_pos):
        """Actualiza el estado hover del botón"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def render(self, surf):
        """Renderiza el botón con el sprite correcto"""
        sprite = self.hover_sprite if self.is_hovered else self.normal_sprite
        surf.blit(sprite, (self.x, self.y))
    
    def is_clicked(self, mouse_pos, mouse_clicked):
        """Verifica si el botón fue clickeado"""
        if self.rect.collidepoint(mouse_pos) and mouse_clicked:
            if self.action:
                self.action()
            return True
        return False

class Menu:
    def __init__(self, game):
        self.game = game
        self.current_menu = "MAIN"  # "MAIN", "CREDITS", "TUTORIAL"
        
        # Crear botones
        self.create_buttons()
        
        # Cargar fondos adicionales si existen
        try:
            self.credits_bg = load_image("Obama PJ/Menu creditos.png", (320, 240))
        except:
            self.credits_bg = self.game.menu_bg
        
        try:
            self.tutorial_bg = load_image("Obama PJ/Menu tutorial.png", (320, 240))
        except:
            self.tutorial_bg = self.game.menu_bg
    
    def create_buttons(self):
        """Crear todos los botones del menú"""
        button_sprites = self.game.assets['buttons']
        
        if len(button_sprites) < 2:
            print("Error: No hay suficientes sprites de botones")
            return
        
        # Botones del menú principal - Diseño: JUGAR a la izquierda, TUTORIAL y CRÉDITOS apilados a la derecha
        
        # Botón JUGAR - izquierda
        self.jugar_button = Button(
            x=80,
            y=150,
            normal_sprite=button_sprites[0] if len(button_sprites) > 0 else pygame.Surface((80, 30)),
            hover_sprite=button_sprites[1] if len(button_sprites) > 1 else pygame.Surface((80, 30)),
            action=self.start_game
        )
        
        # Botón TUTORIAL - arriba derecha
        self.tutorial_button = Button(
            x=200,
            y=120,
            normal_sprite=button_sprites[4] if len(button_sprites) > 4 else button_sprites[0],
            hover_sprite=button_sprites[5] if len(button_sprites) > 5 else button_sprites[1],
            action=self.show_tutorial
        )
        
        # Botón CRÉDITOS - abajo derecha
        self.creditos_button = Button(
            x=200,
            y=170,
            normal_sprite=button_sprites[2] if len(button_sprites) > 2 else button_sprites[0],
            hover_sprite=button_sprites[3] if len(button_sprites) > 3 else button_sprites[1],
            action=self.show_credits
        )
        
        # Botón VOLVER - para créditos y tutorial
        volver_normal = button_sprites[6] if len(button_sprites) > 6 else button_sprites[0]
        volver_hover = button_sprites[7] if len(button_sprites) > 7 else button_sprites[1]
        
        self.volver_button = Button(
            x=20,
            y=200,
            normal_sprite=volver_normal,
            hover_sprite=volver_hover,
            action=self.back_to_main
        )
        
        # Listas de botones por menú
        self.main_buttons = [self.jugar_button, self.tutorial_button, self.creditos_button]
        self.credits_buttons = [self.volver_button]
        self.tutorial_buttons = [self.volver_button]
    
    def start_game(self):
        """Iniciar el juego"""
        self.game.start_game()
    
    def show_credits(self):
        """Mostrar pantalla de créditos"""
        self.current_menu = "CREDITS"
    
    def show_tutorial(self):
        """Mostrar pantalla de tutorial"""
        self.current_menu = "TUTORIAL"
    
    def back_to_main(self):
        """Volver al menú principal"""
        self.current_menu = "MAIN"
    
    def get_scaled_mouse_pos(self):
        """Obtener posición del mouse escalada para la pantalla del juego"""
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0] * 320 // 1054, mouse_pos[1] * 240 // 512)
    
    def update(self):
        """Actualizar botones según el menú actual"""
        scaled_mouse_pos = self.get_scaled_mouse_pos()
        
        if self.current_menu == "MAIN":
            for button in self.main_buttons:
                button.update(scaled_mouse_pos)
        elif self.current_menu == "CREDITS":
            for button in self.credits_buttons:
                button.update(scaled_mouse_pos)
        elif self.current_menu == "TUTORIAL":
            for button in self.tutorial_buttons:
                button.update(scaled_mouse_pos)
    
    def handle_events(self, event):
        """Manejar eventos del menú"""
        scaled_mouse_pos = self.get_scaled_mouse_pos()
        mouse_clicked = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        
        if self.current_menu == "MAIN":
            for button in self.main_buttons:
                button.is_clicked(scaled_mouse_pos, mouse_clicked)
        elif self.current_menu == "CREDITS":
            for button in self.credits_buttons:
                button.is_clicked(scaled_mouse_pos, mouse_clicked)
        elif self.current_menu == "TUTORIAL":
            for button in self.tutorial_buttons:
                button.is_clicked(scaled_mouse_pos, mouse_clicked)
    
    def render_credits_text(self, surf):
        """Renderizar texto de créditos"""
        font = pygame.font.Font(None, 24)
        title_font = pygame.font.Font(None, 32)
        
        # Título
        title = title_font.render("SAVE OBAMA", True, (255, 255, 255))
        title_rect = title.get_rect(center=(160, 30))
        surf.blit(title, title_rect)
        
        # Información de créditos
        credits_lines = [
            "Creadores:",
            "Santiago Chaparro",
            "Dante Zurlo", 
            "Juan Giuri",
            "",
            "Why Always Obama?",
            "",
            "Gracias por jugar!"
        ]
        
        y = 60
        for line in credits_lines:
            if line:
                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(160, y))
                surf.blit(text_surface, text_rect)
            y += 18
    
    def render_tutorial_text(self, surf):
        """Renderizar texto de tutorial"""
        font = pygame.font.Font(None, 20)
        title_font = pygame.font.Font(None, 28)
        
        # Título
        title = title_font.render("COMO JUGAR", True, (255, 255, 255))
        title_rect = title.get_rect(center=(160, 30))
        surf.blit(title, title_rect)
        
        # Instrucciones
        tutorial_lines = [
            "Controles:",
            "",
            "Flechas o WASD para moverse",
            "",
            "Flecha arriba / W: Saltar",
            "Flecha izq / A: Mover izquierda",
            "Flecha der / D: Mover derecha", 
            "",
            "ESC: Volver al menu",
            "",
            "¡Salva a Obama!"
        ]
        
        y = 60
        for line in tutorial_lines:
            if line:
                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(160, y))
                surf.blit(text_surface, text_rect)
            y += 16
    
    def render(self, surf):
        """Renderizar el menú según el estado actual"""
        if self.current_menu == "MAIN":
            # Renderizar fondo del menú principal
            surf.blit(self.game.menu_bg, (0, 0))
            
            # Renderizar botones principales
            for button in self.main_buttons:
                button.render(surf)
                
        elif self.current_menu == "CREDITS":
            # Renderizar fondo de créditos
            surf.blit(self.credits_bg, (0, 0))
            
            # Renderizar texto de créditos
            self.render_credits_text(surf)
            
            # Renderizar botón de volver
            for button in self.credits_buttons:
                button.render(surf)
                
        elif self.current_menu == "TUTORIAL":
            # Renderizar fondo de tutorial
            surf.blit(self.tutorial_bg, (0, 0))
            
            # Renderizar texto de tutorial
            self.render_tutorial_text(surf)
            
            # Renderizar botón de volver
            for button in self.tutorial_buttons:
                button.render(surf)