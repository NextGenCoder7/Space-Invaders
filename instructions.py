import pygame
from constants import *
from utils import *

pygame.init()
pygame.font.init()


def load_text(filename, font, font_size, max_width):
    with open(f'{filename}.txt', 'r') as file:
        return file.read()
    
    words = text.split(' ')
    lines = []
    current_line = []

    text_font = pygame.font.SysFont(font, font_size)

    for word in words:
        current_line.append(word)
        line_width, _ = text_font.size(' '.join(current_line))

        if line_width > max_width:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))

    return lines
    

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
