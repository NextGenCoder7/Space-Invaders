import pygame
from constants import *
from utils import *
from main_menu import main_menu_loop
from instructions import instructions_loop
from scores import scores_loop
from game import game_loop

pygame.init()


def main():
    state = 'main menu'

    run = True
    while run:
        if state == 'main menu':
            current = main_menu_loop(WIN)

            if current == 'playing game':
                state = 'playing game'
            if current == 'instructions':
                state = 'instructions'
            if current == 'scores display':
                state = 'scores display'

        if state == 'playing game':
            current = game_loop(WIN)

            if current == 'game over':
                state = 'game over'

        if state == 'game over':
            # TODO: pass the game's main loop function here
            run = False

        if state == 'instructions':
            current = instructions_loop(WIN)
            
            if current == 'main menu':
                state = 'main menu'
            if current == 'scores display':
                state = 'scores display'

        if state == 'scores display':
            current = scores_loop(WIN)

            if current == 'main menu':
                state = 'main menu'
            if current == 'instructions':
                state = 'instructions'

    pygame.quit()
    quit() 


if __name__ == "__main__":
    main()
