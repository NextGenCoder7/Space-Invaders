import pygame
import os

pygame.font.init()
pygame.mixer.init()


def draw_text_centre(font, text, font_size, color, win):
    text_font = pygame.font.SysFont(font, font_size)
    text_surface = text_font.render(text, True, color)
    win.blit(text_surface, (win.get_width() // 2 - text_surface.get_width() // 2, win.get_height() // 2 - text_surface.get_height() // 2))
    pygame.display.update()


def draw_text(font, text, font_size, color, win, x, y):
    text_font = pygame.font.SysFont(font, font_size)
    text_surface = text_font.render(text, True, color)
    win.blit(text_surface, (x, y))
    pygame.display.update()


def load_sound(file):
    sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', f'{file}.wav'))
    return sound


def load_image(file):
    image = pygame.image.load(os.path.join('assets', 'images', f'{file}.png')).convert_alpha()
    return image


def load_multiple_images(file_prefix, number_of_images):
    images = []

    for i in range(1, number_of_images + 1):
        images.append(pygame.image.load(os.path.join('assets', 'images', f'{file_prefix}{i}.png')).convert_alpha())

    return images
