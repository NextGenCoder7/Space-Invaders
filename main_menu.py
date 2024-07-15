import pygame
from constants import *

pygame.init()


def draw_window_main_menu(win):
    win.fill(BLACK)

    pygame.display.flip()


def main_menu_loop(win):
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

                if event.key == pygame.K_SPACE:
                    return 'playing game'

        draw_window_main_menu(win)

    pygame.quit()
    quit()
