import pygame
from constants import *
from utils import *

pygame.init()
pygame.font.init()

font_path = os.path.join('assets', 'font', 'press_start_2p.ttf')


def load_scores(filename):
    with open(f'{filename}.txt', 'r') as file:
        scores = file.readlines()
        scores = [int(score.strip()) for score in scores]

    top_scores = scores[:120]
    
    save_scores(filename, top_scores)

    return scores


def save_scores(filename, scores):
    with open(f'{filename}.txt', 'w') as file:
        file.write('\n'.join(map(str, scores)))


def calculate_highest_score(filename):
    scores = load_scores(filename)

    return max(scores) if scores else 0


def draw_window_scores(win):
    win.blit(SPACE_BG, (0, 0))

    scores = load_scores('scores')

    y_offset = 20
    x_offset = 20
    column_width = 170
    column_index = 0

    for index, score in enumerate(scores, start=1):
        draw_text('press_start_2p', f'{index}) {score}', 18, YELLOW, win, x_offset + column_index * column_width, y_offset)
        y_offset += pygame.font.Font(font_path, 18).get_linesize()
        y_offset += 10

        if y_offset > HEIGHT - 50:
            y_offset = 20
            column_index += 1

    highest_score = calculate_highest_score('scores')
    draw_text('press_start_2p', f'Highest Score: {highest_score}', 18, YELLOW, win, WIDTH - 350, 20)

    pygame.display.update()


def scores_loop(win):
    clock = pygame.time.Clock()

    # Draw the scores once
    draw_window_scores(win)

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
                
                if event.key == pygame.K_i:
                    return 'instructions'

    pygame.quit()
    quit()
