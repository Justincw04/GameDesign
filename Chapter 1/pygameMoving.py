

import pygame
pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Moving Through Frames")



setBackgroundImage( [  ["dungeonTile.jpg", "dungeonTile.jpg"] ,
                       ["dungeonTile.jpg", "dungeonTile.jpg"]  ])

testSprite  = makeSprite("ashMoving", 20)  # links.gif contains 32 separate frames of animation.

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
        scrollBackground(0, -5)

    elif keyPressed("left"):
        changeSpriteImage(testSprite, 1*5+frame)    # and so on
        scrollBackground(5,0)

    elif keyPressed("up"):
        changeSpriteImage(testSprite,2*5+frame)
        scrollBackground(0,5)

    elif keyPressed("right"):
        changeSpriteImage(testSprite, 3*5+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left

    else:
        changeSpriteImage(testSprite, 0 * 5)  # the static facing front look

    updateDisplay()
    tick(120)



endWait()
