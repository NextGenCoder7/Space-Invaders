import pygame
from constants import *
from utils import *
from buttons import Button

pygame.init()

play_button = Button(WIN, WIDTH // 2 - 150, HEIGHT // 2 - 200, 300, 100, GREEN, WHITE)
instructions_button = Button(WIN, WIDTH // 2 - 250, HEIGHT // 2 - 100, 250, 75, ORANGE, WHITE)
scores_button = Button(WIN, WIDTH // 2, HEIGHT // 2 - 100, 250, 75, YELLOW, WHITE)


def draw_window_main_menu(win, mouse_pos):
    win.blit(SPACE_BG, (0, 0))

    draw_text('press_start_2p', "SPACE INVADERS", 48, BLUE, win, WIDTH // 2 - 320, 10)

    play_button.draw(mouse_pos)
    draw_text('press_start_2p', 'PLAY', 70, GREEN, win, play_button.rect.left + 16, play_button.rect.centery - 27)

    instructions_button.draw(mouse_pos)
    draw_text('press_start_2p', 'INSTRUCTIONS', 20, ORANGE, win, instructions_button.rect.left + 6, instructions_button.rect.centery - 10)
    
    scores_button.draw(mouse_pos)
    draw_text('press_start_2p', 'SCORES', 40, YELLOW, win, scores_button.rect.left + 9, scores_button.rect.centery - 20)

    win.blit(DUMMY_SPACESHIP, (450, 550))

    pygame.display.update()


def main_menu_loop(win):
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

                if event.key == pygame.K_SPACE:
                    return 'playing game'
                
                if event.key == pygame.K_i:
                    return 'instructions'
                
                if event.key == pygame.K_s:
                    return 'scores display'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if play_button.is_clicked(mouse_pos):
                        return 'playing game'
                    if instructions_button.is_clicked(mouse_pos):
                        return 'instructions'
                    if scores_button.is_clicked(mouse_pos):
                        return 'scores display'
                
        draw_window_main_menu(win, mouse_pos)

    pygame.quit()
    quit()
