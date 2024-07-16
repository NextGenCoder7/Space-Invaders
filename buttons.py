import pygame

pygame.init()


class Button:

    def __init__(self, win, x, y, width, height, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.win = win

    def draw(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.win, self.hover_color, self.rect, 3)
        else:
            pygame.draw.rect(self.win, self.color, self.rect, 3)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
