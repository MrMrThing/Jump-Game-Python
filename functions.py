import pygame
import random
from pygame.display import update

platform_height = []
platform_width = []

platform_X = []
platform_y = []

ready_jump = False

def setup():
    for x in 10:
        platform_y[x] = x*50
        platform_X[x] = random.randint(10,600)
        platform_height[x] = 10
        platform_width[x] = random.randint(50,100)

def draw(screen, x, y, player_width, player_height):

    for x in 10:
        pygame.draw.rect(screen, (200,200,0), (platform_X[x], platform_y[x], platform_width[x], platform_height[x]))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, player_width, player_height))
    

def collision(gravity, x, y, collision_check, fall_speed):
    if(y < platform_y - platform_height - 7 and not y < platform_y - platform_height - 10 and x > platform_X - 15 and x < platform_X + platform_width - 5):
        if(collision_check == False):
            gravity = 0
            collision_check = True
    else:
        if(gravity < 2):
            gravity += fall_speed
            collision_check = False

    return gravity
      
def jump(y):

    for x in 10:
        if(y < platform_y[x]  and not y < platform_y[x] - 23):
            ready_jump = True
        else:
            ready_jump = False
        return ready_jump