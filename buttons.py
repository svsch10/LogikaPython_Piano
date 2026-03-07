# from pygame import Rect, mouse, transform, image, MOUSEBUTTONDOWN, draw
import pygame
from settings import BLACK, GREY, DARK_GREY

class Button:
    def __init__(self, x, y, width, height, text: str = "", action=None, img_idle=None, img_hover=None, center: bool = False):
        self.text = text
        self.action = action
        self.img_idle = img_idle
        self.img_hover = img_hover
        # self.use_image = img_idle is not None
        if img_idle is not None:
            self.use_image = True
        else:
            self.use_image = False

        self.color_idle = GREY
        self.color_hover = DARK_GREY
        self.color_border = BLACK
        self.text_color = BLACK

        if self.use_image and (width is None or height is None):
            iw, ih = self.img_idle.get_size()    # image_width, image_height
            width = width or iw
            height = height or ih

        if center:
            self.rect = pygame.Rect(0, 0, width, height)
            self.rect.center = (x, y)
        else:
            self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, font):
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(mouse_pos)

        if self.use_image:
            # surf = (self.img_hover if (hovered and self.img_hover) else self.img_idle)
            if hovered and self.img_hover:
                surf = self.img_hover
            else:
                surf = self.img_idle
            
            if surf.get_size() != (self.rect.w, self.rect.h):
                surf = transform.scale(surf, (self.rect.w, self.rect.h))
            screen.blit(surf, self.rect.topleft)

            if self.text:
                text_surf = font.render(self.text, True, self.text_color)
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))
        else:
            # color = self.color_hover if hovered else self.color_idle
            if hovered:
                color = self.color_hover
            else:
                color = self.color_idle
            draw.rect(screen, color, self.rect, border_radius=8)
            draw.rect(screen, self.color_border, self.rect, 2, border_radius=8)

            if self.text:
                text_surf = font.render(self.text, True, self.text_color)
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            if self.action:
                self.action()
