import pygame
from utils import load_image, load_multiple_images

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

SPACE_BG_PATH = load_image('bg')
SPACE_BG = pygame.transform.scale(SPACE_BG_PATH, (WIDTH, HEIGHT))

SPACESHIP_PATH = load_image('spaceship')
DUMMY_SPACESHIP = pygame.transform.scale(SPACESHIP_PATH, (200, 200))
