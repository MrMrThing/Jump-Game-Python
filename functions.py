import pygame
import random
from pygame.display import update

# Here we get all the variables and draw the platforms and player
def draw(screen, x, y, player_width, player_height, platform_height, platform_width, platform_X, platform_y, platform_speed):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, player_width, player_height)) # Drawing player

    # for loop, drawing all the platforms, and updates there positions to the top, if they are to far down
    for x in range(len(platform_X)):
        pygame.draw.rect(screen, (200,200,0), (platform_X[x], platform_y[x], platform_width[x], platform_height[x])) # drawing the platform
        platform_y[x] += platform_speed # updating the platform Y coordinat, according to the speed

        # Setting the platforms to the top, if they are under the screen
        if(platform_y[x] > 810):
            platform_y[x] = 0
            platform_X[x] = random.randint(10,400)


# checking if the player is standing on one of the platforms
def collision(gravity, x, y, fall_speed, player_width, platform_height, platform_width, platform_X, platform_y):   
    # 2 variables that is used
    ready_jump = False 
    collision_check = False

    # this for loop check all the platforms, and see if the player is on top
    for i in range(len(platform_X)): 
        if(y <= platform_y[i] - platform_height[i] and y >= platform_y[i] - platform_height[i] - 10 and x >= platform_X[i] - player_width and x <= platform_X[i] + platform_width[i]):
            gravity = 0 # if the player is on top, don't let them fall down
            collision_check = True 

            # There is a little bug, for then the platforms fall down, and the player fall with
            # half the time the player is technically not touching the platform
            # So we just check if they are a little futher above 
            if(y < platform_y[i]  and not y < platform_y[i] - 25): 
                ready_jump = True
            else:
                ready_jump = False
            
    if(collision_check == False): # if the player has not touched any of the platforms, make them fall down
        if(gravity < 2):
            gravity += fall_speed

    return gravity, ready_jump # send the gravity and ready_jump back to the main

# Rasmus Rosendal Nielsen