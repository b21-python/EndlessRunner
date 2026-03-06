#Import pygame module
import pygame
from pygame.locals import *

#Initialize the pygame
pygame.init()

####constants####
#Colors
GREEN = (100, 100, 42) 
ORANGE = (255, 102, 0) 
#Accessors
X = 0
Y = 1
W = 2
H = 3

####game variables####

#Player state       X   Y   W   H
player = { "Area":[10, 10, 180, 40], "Color":ORANGE, "Speed":1 }

groundlevel = 400

#game window size
width = 640
height = 480

#game window
screen = pygame.display.set_mode([width, height])

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = { K_a:0, K_d:0, K_w:0, K_s:0 }

#keeps time for game
gameClock = pygame.time.Clock()

gameActive = True

obstacles = [Rect(width, groundlevel - 20, 20, 20),
            Rect(width + 300, -20, 60, 40),
            Rect(width + 380 , -20, 80, 40)]
            





#Main Game loop.  The game runs until the user quits
while gameActive:

    #Limit to 60 FPS
    gameClock.tick(200)

    #Fill screen with bg color
    screen.fill(GREEN)

    pygame.draw.rect(screen, player["Color"], player["Area"])
    
    pygame.draw.rect(screen, ORANGE, [0, groundlevel, width, height - groundlevel])
    for ob in obstacles:
         pygame.draw.rect(screen, "brown", ob)
         
    for ob in obstacles:
        ob.move_ip(-groundspeed, 0)
    
    #Draw arena (surface)
    pygame.display.update()

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = player["Speed"]
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.QUIT:             #The user quit
            gameActive = False

    #Determine new player position based on keyboard input
    xMovement = keys[K_d] - keys[K_a]
    yMovement = keys[K_s] - keys[K_w]
    updatedX = player["Area"][X] + xMovement
    updatedY = player["Area"][Y] + yMovement

    #Update player position if new position is in bounds
    if updatedX >= 0 and updatedX + player["Area"][W] <= width:
        player["Area"][X] = updatedX
    if updatedY >= 0 and updatedY + player["Area"][H] <= groundlevel:
        player["Area"][Y] = updatedY
        

#end pygame
pygame.quit()
# Make list  add obstacles right after change height to ground level
# every frame change the x postion by however pixel
# Finish the list

