import pygame
from constants import *
from utils import *

pygame.init()
pygame.font.init()

font_path = os.path.join('assets', 'font', 'press_start_2p.ttf')


def load_text(filename, font_name, font_size, max_width):
    with open(f'{filename}.txt', 'r') as file:
        text = file.read()
    
    lines = text.split('\n')
    wrapped_lines = []

    text_font = pygame.font.Font(font_path, font_size)

    for line in lines:
        words = line.split(' ')
        current_line = []

        for word in words:
            current_line.append(word)
            line_width, _ = text_font.size(' '.join(current_line))

            if line_width > max_width:
                current_line.pop()
                wrapped_lines.append(' '.join(current_line))
                current_line = [word]

        wrapped_lines.append(' '.join(current_line))

    return wrapped_lines


def draw_window_instructions(win):
    win.blit(SPACE_BG, (0, 0))
    
    instructions_lines = load_text('instructions', 'press_start_2p', 21, WIDTH - 100)
    y_offset = 20

    for line in instructions_lines:
        draw_text('press_start_2p', line, 21, WHITE, win, 50, y_offset)
        y_offset += pygame.font.Font(font_path, 21).get_linesize()

    pygame.display.update()


def instructions_loop(win):
    clock = pygame.time.Clock()

    # Draw the instructions once
    draw_window_instructions(win)

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
                
                if event.key == pygame.K_s:
                    return 'scores display'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()
    quit()
