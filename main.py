import pygame
from functions import * # importing the functions from the other file

pygame.init() # Starting pygame
  

screen = pygame.display.set_mode((500, 800))    # Setting the window size
  
pygame.display.set_caption("Game") # Setting an title to the window

# Player X and Y coordinates
x = 400
y = 100
  
# Size of the player  
player_width = 20
player_height = 20

platform_speed = 0.2

player_speed = 2
player_jump = -3.5 # jump height
gravity = 2 # How fast the player falls
fall_speed = 0.05 # How fast the player accelerates 
  
number_of_platforms = 15

# Making and setting the different platforms
platform_height = [10 for x in range(number_of_platforms)]
platform_width = [random.randint(50,100) for x in range(number_of_platforms)]

platform_X = [random.randint(10,400) for x in range(number_of_platforms)]
platform_y = [x*50 for x in range(number_of_platforms)]

score = 0

# Color and font, for the score text
font_color=(0,150,250)
font_obj=pygame.font.SysFont("Comic Sans ms",25)

ready_jump = False # Checking if the player can jump

# Indicates pygame is running
run = True

# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)

    score += 0.1 
    if(int(score) % 10 == 0):
        platform_speed += 0.002
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
      if(ready_jump == True): # Can the player jump
        gravity = player_jump
          
    
    screen.fill((50, 50, 50)) # Setting the background color
          
    # updating the gravity and ready_jump, with the collision function
    gravity, ready_jump = collision(gravity, x, y, fall_speed, player_width, platform_height, platform_width, platform_X, platform_y)
    
    y = y + gravity # updating the players position with gravity

    # calling function to draw what should be on screen
    draw(screen, x, y, player_width, player_height, platform_height, platform_width, platform_X, platform_y, platform_speed)

    # setting the score text up
    text_obj = font_obj.render("Score: " +str(int(score)),True,font_color)
    screen.blit(text_obj,(50,30))

    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()

# Rasmus Rosendal Nielsen