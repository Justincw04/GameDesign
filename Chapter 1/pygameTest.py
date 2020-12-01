#Justin Cortez Wartell

#Pygame work
#background color
import pygame, time, sys
#asking the user for a color
pygame.init()
#Background picture should be the size of your screen
backdrop=pygame.image.load('Background.png')
tempSprite=pygame.image.load('dht11.jpg')
pygame.time.delay(100)
WIDTH=1000
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
white=[255,255,255]
red=[255,0,0]
green = [0,255,0]

screen.fill(white)
pygame.display.set_caption("My Shapes")
pygame.display.flip()
running = True

walkRight = [pygame.image.loaf('Stripe\R1E.png')

#VAriables to control objects
x=29
y=20
w=32
h=64
r=30
Jump=False
high=10
def redrawWindow():
    screen.blit(backdrop, (0,0))
    screen.blit(tempSprite,(x,y))
    pygame.draw.rect(screen,(10,123,10),(x,y,w,h))
    pygame.display.update()
walkCount - 0
def redrawGamescreendow():
    global walkCount

    screen.blit(bg, (0,0))
    of walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkcount+= 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkcount+= 1
    else:
        screen.blit(character, (x,y))
        walkCount = 0
while running:
    clock.tick(27)
    #screen.fill(white)
    #Background image on the screen

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pygame.time.delay(100)
    #                window    color     x, y   w   h

    # We are going to move our rectnagle around
    keyBoardKey=pygame.key.get_pressed()
    #check what key was pressed
    speed = 10
    if keyBoardKey[pygame.K_LEFT] and x > speed:  # I need to substract from x
        x -= speed
        r -= speed
    if keyBoardKey[pygame.K_RIGHT] and x < WIDTH - w - speed:  # I need to add to the x
        x += speed
        r += speed
    if not(Jump): #this is for moving y without a jump
        if keyBoardKey[pygame.K_UP] and y > speed:     # I need to substract to the y
            y -= speed
        if keyBoardKey[pygame.K_DOWN] and y < HEIGHT - h - speed:    # I need to add to the y
            y += speed
        if keyBoardKey[pygame.K_SPACE]:
            Jump=True
            left - False
            right = False
            walkCount = 0
    else:
        if high >= -10:
            y -= (high * abs(high)) /2
            high -= 1
        else:
            high = 10
            jump = False

    redrawWindow()

pygame.quit()
