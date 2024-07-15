import pygame
from constants import *
from utils import *

pygame.init()
pygame.font.init()


def load_scores(filename):
    with open(f'{filename}.txt', 'r') as file:
        scores = file.readlines()
        scores = [int(score.strip()) for score in scores]

    scores.sort(reverse=True)
    top_scores = scores[:300]
    
    save_scores(filename, top_scores)

    return scores


def save_scores(filename, scores):
    with open(f'{filename}.txt', 'w') as file:
        file.write('\n'.join(map(str, scores)))


def calculate_highest_score(filename):
    scores = load_scores(filename)

    return max(scores) if scores else 0


def draw_window_scores(win):
    win.fill(BLACK)

    scores = load_scores('scores')

    y_offset = 20
    x_offset = 20
    column_width = 130
    column_index = 0

    for index, score in enumerate(scores, start=1):
        draw_text('comicsans', f'{index}. {score}', 24, WHITE, win, x_offset + column_index * column_width, y_offset)
        y_offset += pygame.font.SysFont('comicsans', 24).get_linesize()

        if y_offset > HEIGHT - 50:
            y_offset = 20
            column_index += 1

    highest_score = calculate_highest_score('scores')
    draw_text('comicsans', f'Highest Score: {highest_score}', 24, WHITE, win, WIDTH - 250, 20)

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
