import pygame
from utils import *
from constants import *

pygame.init()


class Player(pygame.sprite.Sprite):
    VEL = 5
    MAX_HEALTH = 100

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(SPACESHIP_PATH, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = self.VEL
        self.mask = pygame.mask.from_surface(self.image)
        self.health = self.MAX_HEALTH

    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    