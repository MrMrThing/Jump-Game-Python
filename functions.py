import pygame
from pygame.display import update



def draw(screen, platform_X, platform_y, platform_width, platform_height, x, y, player_width, player_height):
    pygame.draw.rect(screen, (200,200,0), (platform_X, platform_y, platform_width, platform_height))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, player_width, player_height))
    

def collision(gravity, platform_y, platform_width, platform_height, x, y, collision_check, platform_X, fall_speed):
    if(y < platform_y - platform_height - 7 and not y < platform_y - platform_height - 10 and x > platform_X - 15 and x < platform_X + platform_width - 5):
        if(collision_check == False):
            gravity = 0
            collision_check = True
    else:
        if(gravity < 2):
            gravity += fall_speed
            collision_check = False

    return gravity
      