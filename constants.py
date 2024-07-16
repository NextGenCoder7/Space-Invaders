import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1100, 900

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

FPS = 60

# List of colors in their RGB values
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

SPACE_BG = pygame.image.load(os.path.join('assets', 'images', 'bg.png'))
SPACE_BG = pygame.transform.scale(SPACE_BG, (WIDTH, HEIGHT))
