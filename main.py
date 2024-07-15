import pygame
from constants import *
from utils import *
from main_menu import main_menu_loop

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


def main():
    state = 'main menu'

    run = True
    while run:
        if state == 'main menu':
            current = main_menu_loop(WIN)
            if current == 'playing game':
                state = 'playing game'

        if state == 'playing game':
            # TODO: pass the playing game's main loop function here
            run = False

        if state == 'game over':
            # TODO: pass the game's main loop function here
            run = False

    pygame.quit()
    quit() 


if __name__ == "__main__":
    main()
