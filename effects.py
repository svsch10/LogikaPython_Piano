import pygame
from settings import BLACK

def draw_key_effect(screen, rect, is_pressed=False):
    if not is_pressed:
        base_color = LIGHT_GREY
    else:
        base_color = LIGHT_BLUE
    border_color = BLACK
    
    pygame.draw.rect(screen, base_color, rect, border_radius=8)
    pygame.draw.rect(screen, border_color, rect, 2, border_radius=8)
