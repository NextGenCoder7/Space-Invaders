import pygame
from constants import *
from utils import *
from buttons import Button

pygame.init()
pygame.font.init()

font_path = os.path.join('assets', 'font', 'press_start_2p.ttf')

scores_button = Button(WIN, 200, HEIGHT - 70, 200, 60, YELLOW, WHITE)
main_menu_button = Button(WIN, WIDTH - 430, HEIGHT - 70, 200, 60, BLUE, WHITE)


def load_text(filename, font_size, max_width):
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


def draw_window_instructions(win, mouse_pos):
    win.blit(SPACE_BG, (0, 0))

    scores_button.draw(mouse_pos)
    draw_text('press_start_2p', 'SCORES', 31, YELLOW, win, scores_button.rect.left + 9, scores_button.rect.centery - 15)

    main_menu_button.draw(mouse_pos)
    draw_text('press_start_2p', 'MAIN MENU', 21, BLUE, win, main_menu_button.rect.left + 8, main_menu_button.rect.centery - 11)
    
    instructions_lines = load_text('instructions', 21, WIDTH - 100)
    y_offset = 20

    for line in instructions_lines:
        draw_text('press_start_2p', line, 21, ORANGE, win, 50, y_offset)
        y_offset += pygame.font.Font(font_path, 21).get_linesize()

    pygame.display.update()


def instructions_loop(win):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

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
                if event.button == 1:

                    if scores_button.is_clicked(mouse_pos):
                        return'scores display'
                    if main_menu_button.is_clicked(mouse_pos):
                        return 'main menu'

        draw_window_instructions(win, mouse_pos)

    pygame.quit()
    quit()
