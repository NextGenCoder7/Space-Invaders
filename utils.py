import pygame
import os

pygame.init()
pygame.font.init()


def draw_text_centre(font_name, text, font_size, color, win):
    font_path = os.path.join('assets', 'font', f'{font_name}.ttf')
    text_font = pygame.font.Font(font_path, font_size)
    text_surface = text_font.render(text, True, color)
    win.blit(text_surface, (win.get_width() // 2 - text_surface.get_width() // 2, win.get_height() // 2 - text_surface.get_height() // 2))


def draw_text(font_name, text, font_size, color, win, x, y):
    font_path = os.path.join('assets', 'font', f'{font_name}.ttf')
    text_font = pygame.font.Font(font_path, font_size)
    text_surface = text_font.render(text, True, color)
    win.blit(text_surface, (x, y))


def load_image(filename):
    return pygame.image.load(os.path.join('assets', 'images', f'{filename}.png')).convert_alpha()


def load_multiple_images(file_prefix, number_of_images, scale=False, width=0, height=0):
    images = []

    for i in range(1, number_of_images + 1):
        image_path = os.path.join('assets', 'images', f'{file_prefix}{i}.png')
        image = pygame.image.load(image_path).convert_alpha()
        
        if scale:
            image = pygame.transform.scale(image, (width, height))
        
        images.append(image)

    return images
