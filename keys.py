from pygame import Rect, transform, image
from effects import *

# --- Картинка з зображенням клавіші ---
KEY_UNPRESSED = transform.scale(image.load('assets/images/key_unpressed.png'), (100, 250))

def create_key_rects(num_keys, start_x=50, start_y=100, key_width=100,
                     key_height=250):
    rects = []
    for i in range(num_keys):
        x = start_x + i * key_width
        rects.append(Rect(x, start_y, key_width, key_height))
    return rects

def draw_keys(screen, key_rects, pressed_keys):
    pressed_set = set(pressed_keys)

    for i, rect in enumerate(key_rects):
        # is_pressed = i in pressed_set
        is_pressed = i in pressed_keys
        screen.blit(KEY_UNPRESSED, (rect.x, rect.y))
