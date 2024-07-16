import pygame
from constants import *
from utils import *

pygame.init()


def draw_window_main_menu(win):
    win.blit(SPACE_BG, (0, 0))

    draw_text('press_start_2p', "SPACE INVADERS", 48, BLUE, win, WIDTH // 2 - 300, 10)

    pygame.display.flip()


def main_menu_loop(win):
    clock = pygame.time.Clock()

    # draw window once
    draw_window_main_menu(win)

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
                
                if event.key == pygame.K_i:
                    return 'instructions'
                
                if event.key == pygame.K_s:
                    return 'scores display'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()
    quit()
