#Justin Cortez Wartell
#Final Project Game
import pygame
import pygame_functions
from pygame_functions import *
pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Moving Through Frames")

bg = pygame.image.load("//Users//Justin//github//GameDesign//Chapter 1//dungeonTile.jpg")

testSprite  = makeSprite("//Users//Justin//github//GameDesign//Chapter 1//ashMoving.gif", 20)  # links.gif contains 32 separate frames of animation.

moveSprite(testSprite,300,300,True)
showSprite(testSprite)

nextFrame = clock()
frame = 0
while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1)%5                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop





    if keyPressed("down"):
        changeSpriteImage(testSprite, 0*5+frame)    # down facing animations are the 1st set
        background.scroll(0, -5)

    elif keyPressed("left"):
        changeSpriteImage(testSprite, 1*5+frame)    # and so on
        background.scroll(5,0)

    elif keyPressed("up"):
        changeSpriteImage(testSprite,2*5+frame)
        background.scroll(0,5)

    elif keyPressed("right"):
        changeSpriteImage(testSprite, 3*5+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        background.scroll(-5,0)                      # The player is moving right, so we scroll the background left

    else:
        changeSpriteImage(testSprite, 0 * 5)  # the static facing front look

    pygame.display.update()
    tick(120)



endWait()
