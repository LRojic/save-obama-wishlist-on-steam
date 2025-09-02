class Button():
    def __init__(self, image_normal, image_hover, pos, text_input, font, base_color, hovering_color):
        self.image_normal = image_normal
        self.image_hover = image_hover
        self.current_image = image_normal
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.current_image is None:
            self.current_image = self.text
        self.rect = self.current_image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.current_image is not None:
            screen.blit(self.current_image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.current_image = self.image_hover
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.current_image = self.image_normal
            self.text = self.font.render(self.text_input, True, self.base_color)