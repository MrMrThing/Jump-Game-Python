import pygame
from functions import draw,collision

pygame.init()
  
screen = pygame.display.set_mode((500, 800))
  
pygame.display.set_caption("Game")
  
x = 200
y = 100
  
player_width = 20
player_height = 20

platform_height = 10
platform_width = 50

platform_X = 200
platform_y = 350
  
player_speed = 2
player_jump = -3.5
gravity = 2
fall_speed = 0.05
  
collision_check = False
ready_jump = False

# Indicates pygame is running
run = True


# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
            run = False

    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    if keys[pygame.K_LEFT] and x>0:
        x -= player_speed
          

    if keys[pygame.K_RIGHT] and x<500-player_width:
        x += player_speed
         

    if keys[pygame.K_UP] and y>0:
      if(ready_jump == True):
        gravity = player_jump
          
    
    if(y < platform_y  and not y < platform_y - 23):
      ready_jump = True
    else:
      ready_jump = False

    
    screen.fill((50, 50, 50))   
          
    # completely fill the surface object  
    # with black colour  
    gravity = collision(gravity, platform_y, platform_width, platform_height, x, y, collision_check, platform_X, fall_speed)
    
    y = y + gravity 
    platform_y += 0.2
    draw(screen, platform_X, platform_y, platform_width, platform_height, x, y, player_width, player_height)

    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()

