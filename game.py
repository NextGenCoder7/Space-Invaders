import pygame
from constants import *
from utils import *
from player import Player

pygame.init()

player = Player(WIDTH // 2, HEIGHT - 100, 64, 64)   


def draw_window_game(win, keys):
    win.blit(SPACE_BG, (0, 0))

    player.update(keys)
    player.draw(win)

    pygame.display.update()


def game_loop(win):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    run = False

        keys = pygame.key.get_pressed()

        if player.health <= 0:
            return 'game over'

        draw_window_game(win, keys)

    pygame.quit()
    quit()
