import pygame
from constants import WHITE

pygame.init()


class Button:

    def __init__(self, win, x, y, width, height, color, hover):
        self.rect = pygame.rect(x, y, width, height)
        self.color = color
        self.width = width
        self.height = height
        self.hover = hover
        self.win = win

    def draw(self):
        if self.hover:
            pygame.draw.rect(self.win, WHITE, self.rect, 3)
        else:
            pygame.draw.rect(self.win, self.color, self.rect, 3)

    def is_clicked(self, mouse_pos):
        x, y = mouse_pos
        
        return self.rect.collidepoint(x, y)
