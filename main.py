import pygame
  


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
  
speed = 2
gravity = 5
  
collision = False

# Indicates pygame is running
run = True
  
def draw():
  pygame.draw.rect(screen, (200,200,0), (platform_X, platform_y, platform_width, platform_height))
  pygame.draw.rect(screen, (255, 0, 0), (x, y, player_width, player_height))
  


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
        x -= speed
          

    if keys[pygame.K_RIGHT] and x<500-player_width:
        x += speed
         

    if keys[pygame.K_UP] and y>0:
      if(collision == True):
        gravity = -2
          
    if(y < platform_y - platform_height - 7 and not y < platform_y - platform_height - 10 and x > platform_X - 15 and x < platform_X + platform_width - 5):
      if(collision == False):
        gravity = 0
      collision = True

    else:
      if(gravity < 2):
        gravity += 0.02
      collision = False
      
    y = y + gravity   
    screen.fill((50, 50, 50))         
    # completely fill the surface object  
    # with black colour  
    
    platform_y += 0.2
      
    # drawing object on screen which is rectangle here 
    
    draw()
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()


