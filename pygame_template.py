# This codee

import pygame
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

BOING_SOUND = pygame.mixer.Sound("boing.wav")

SCREEN_WIDTH = 800                # Height of the playing field.
SCREEN_HEIGHT = 800               # Width of the playing field.

# Player Variables
playerX = int(SCREEN_WIDTH / 2)   # This starts the player X at the midway point.
playerY = int(SCREEN_HEIGHT/ 2)   # This starts the player Y at the midway point.
velocity = 5                      # The 'player' starts out moving.
direction = None                  # But has no direction.
playerSize = 50                   # This is the radius of the circle.

# Now that pygame is imported and initialized
# we need a screen
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

# Run until not true
running = True
while running:

    # did we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # This part of the loop detects keys pressed.
        pressed = pygame.key.get_pressed()     
        if (pressed[K_RIGHT] or pressed[K_d]):
            direction = 'east'
        if (pressed[K_LEFT] or pressed[K_a]):
            direction = 'west'
        if (pressed[K_UP] or pressed[K_w]):
            direction = 'north'
        if (pressed[K_DOWN] or pressed[K_s]):
            direction = 'south'
        if (pressed[K_SPACE]):
            velocity += 5

    # Do logical updates here
    # This is how we bounce
    if playerX < 0 or playerX > SCREEN_WIDTH:   # If the player location is at the screen edge,
        pygame.mixer.Sound.play(BOING_SOUND)    # play a sound
        velocity = -velocity                    # and flip the velocity so you are moving in the 
                                                # opposite direction.
    # This is how we loop off screen
    if playerY < 0:                             # If we are at the screen edge
        playerY = SCREEN_HEIGHT                 # set the position to the opposite screen edge.
    if playerY > SCREEN_HEIGHT:
        playerY = 0

    
    if direction == 'east':
        playerX += velocity
    if direction == 'west':
        playerX -= velocity
    if direction == 'north':
        playerY -= velocity
    if direction == 'south':
        playerY += velocity

    # Fill the screen with a color
    screen.fill(GREEN)

    # draw something, a dot
    pygame.draw.circle(screen, (0, 0, 255), (playerX, playerY), playerSize)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit
pygame.quit()
