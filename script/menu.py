# menu.py
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
        
        # Crear rect para detectar colisiones
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
        self.main_buttons = []
        self.credits_buttons = []
        self.current_menu = "MAIN"  # "MAIN", "CREDITS"
        
        # Cargar fondo de créditos si lo tenés
        self.credits_bg = None
        try:
            self.credits_bg = load_image("Obama PJ/Menu creditos.png", (320, 240))
        except:
            # Si no tenés fondo de créditos, usa el mismo del menú principal
            self.credits_bg = load_image("Obama PJ/Menu chad sin botones.png", (320, 240))
        
        self.create_main_buttons()
        self.create_credits_buttons()
    
    def create_main_buttons(self):
        """Crea los botones del menú principal"""
        button_sprites = self.game.assets['buttons']
        
        # Asumiendo orden: jugar_normal, jugar_hover, creditos_normal, creditos_hover, 
        # tutorial_normal, tutorial_hover, salir_normal, salir_hover
        if len(button_sprites) >= 8:
            # Botón JUGAR
            jugar_button = Button(
                x=120,  # Ajustá estas posiciones según tu diseño
                y=100,
                normal_sprite=button_sprites[0],  # jugar normal
                hover_sprite=button_sprites[1],   # jugar hover
                action=self.start_game
            )
            
            # Botón CRÉDITOS
            creditos_button = Button(
                x=120,
                y=135,
                normal_sprite=button_sprites[2],  # creditos normal
                hover_sprite=button_sprites[3],   # creditos hover
                action=self.show_credits
            )
            
            # Botón TUTORIAL
            tutorial_button = Button(
                x=120,
                y=170,
                normal_sprite=button_sprites[4],  # tutorial normal
                hover_sprite=button_sprites[5],   # tutorial hover
                action=self.show_tutorial
            )
            
            # Botón SALIR
            salir_button = Button(
                x=120,
                y=205,
                normal_sprite=button_sprites[6],  # salir normal
                hover_sprite=button_sprites[7],   # salir hover
                action=self.quit_game
            )
            
            self.main_buttons = [jugar_button, creditos_button, tutorial_button, salir_button]
        else:
            print("Error: No hay suficientes sprites de botones")
    
    def create_credits_buttons(self):
        """Crea los botones del menú de créditos"""
        button_sprites = self.game.assets['buttons']
        
        # Botón SALIR para volver del menú de créditos (reutilizamos el sprite de salir)
        if len(button_sprites) >= 8:
            volver_button = Button(
                x=20,   # Posición en una esquina
                y=200,
                normal_sprite=button_sprites[6],  # salir normal (o podés usar otro sprite)
                hover_sprite=button_sprites[7],   # salir hover
                action=self.back_to_main
            )
            
            self.credits_buttons = [volver_button]
    
    def start_game(self):
        """Inicia el juego"""
        print("¡Iniciando juego!")
        self.game.game_state = "PLAYING"
    
    def show_credits(self):
        """Muestra la pantalla de créditos"""
        print("Mostrando créditos...")
        self.current_menu = "CREDITS"
    
    def show_tutorial(self):
        """Muestra el tutorial"""
        print("Mostrando tutorial...")
        # Acá podés agregar lógica para mostrar tutorial
        # Por ejemplo, cambiar a un estado "TUTORIAL"
        pass
    
    def back_to_main(self):
        """Vuelve al menú principal"""
        print("Volviendo al menú principal...")
        self.current_menu = "MAIN"
    
    def quit_game(self):
        """Sale del juego"""
        import sys
        pygame.quit()
        sys.exit()
    
    def update(self, mouse_pos, mouse_clicked):
        """Actualiza el menú según el estado actual"""
        if self.current_menu == "MAIN":
            for button in self.main_buttons:
                button.update(mouse_pos)
                button.is_clicked(mouse_pos, mouse_clicked)
        elif self.current_menu == "CREDITS":
            for button in self.credits_buttons:
                button.update(mouse_pos)
                button.is_clicked(mouse_pos, mouse_clicked)
    
    def render(self, surf):
        """Renderiza el menú según el estado actual"""
        if self.current_menu == "MAIN":
            # Renderizar fondo del menú principal
            menu_bg = load_image("Obama PJ/Menu chad sin botones.png", (320, 240))
            surf.blit(menu_bg, (0, 0))
            
            # Renderizar botones principales
            for button in self.main_buttons:
                button.render(surf)
                
        elif self.current_menu == "CREDITS":
            # Renderizar fondo de créditos
            surf.blit(self.credits_bg, (0, 0))
            
            # Acá podés agregar texto de créditos si querés
            self.render_credits_text(surf)
            
            # Renderizar botón de volver
            for button in self.credits_buttons:
                button.render(surf)
    
    def render_credits_text(self, surf):
        """Renderiza el texto de los créditos"""
        # Ejemplo de texto de créditos
        font = pygame.font.Font(None, 24)
        credits_lines = [
            "SAVE OBAMA",
            "",
            "Desarrollado por: Tu Nombre",
            "Música: Artista Musical", 
            "Arte: Artista Visual",
            "",
            "Gracias por jugar!"
        ]
        
        y_offset = 50
        for line in credits_lines:
            if line:  # Si la línea no está vacía
                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(160, y_offset))
                surf.blit(text_surface, text_rect)
            y_offset += 20