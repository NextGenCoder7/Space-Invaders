import pygame
from constants import *
from utils import *

pygame.init()


def load_text(filename):
    with open(f'{filename}.txt', 'r') as file:
        return file.read()
    
        # TODO: wrap the text so that it fits in the screen
    

def draw_window_instructions(win):
    win.fill(BLACK)

    instructions_text = load_text('instructions')
    draw_text('comicsans', instructions_text, 24, WHITE, win, 10, 10)

    pygame.display.flip()
    

def instructions_loop(win):
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

                if event.key == pygame.K_m:
                    return 'main menu'

        draw_window_instructions(win) 

    pygame.quit()
    quit()
