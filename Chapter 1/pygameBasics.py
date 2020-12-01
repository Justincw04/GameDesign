#Justin Cortez Wartell
import pygame
import time
import sys
#asking for color
pygame.init()
pygame.time.delay(100)
screen=pygame.display.set_mode((800,800))
white=[255,255,255]
red=[255,0,0]
green=[0,255,0]
screen.fill(red)
pygame.display.set_caption("My game")
pygame.display.update()
pygame.time.delay(1000)
screen.fill(white)
pygame.display.set_caption("Your game ")
pygame.display.flip()
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, )
pygame.quit()








pygame.time.delay(100)
#                window    color       x, y   w h
pygame.draw.rect(screen,(10,123,10),(20,20 50,100))
pygame.display.update()
#we are going to move our rectangle background
pygame.draw.circle(screen,(0,120,129), (x+100, y+100),50, 4)
pygame.display.update()
keyBoardKey=pygame.key.get_pressed()
#check what key is get_pressed
speed=1
if keyBoardKey[pygame_.K_LEFT]:
    x-= speed


if keyBoardKey[pygame_.K_RIGHT]:
    x+= speed


if keyBoardKey[pygame_.K_UP]:
    y-= speed


if keyBoardKey[pygame_.K_DOWN]:
    y+= speed



#                 windown   color       position, radius, thick
#pygame.draw.circle(screen,(0,120,129), (100,100),30, 4)
#pygame.display.update()
pygame.quit()
