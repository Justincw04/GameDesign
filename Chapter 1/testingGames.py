import pygame
import time
import random
import sys
pygame.init()



b = 20
a = 20
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

RADIUS = 10
WIDTH = 1600
HEIGHT = 800
run = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
#menu with instruction list and difficulty selector
def menu():
    screen.fill(white)
    text = TITLE_FONT.render("Let's Play Snake!", 1, black)

    #instructions
    text = LETTER_FONT.render("In this game, use your arrow keys to move the direction of your snake. Eat food to grow longer and earn points.", 1, black)
    text2 = LETTER_FONT.render("If you hit a wall or hit your own snake, you will lose", 1, black)
    text3 = LETTER_FONT.render("First, choose your difficulty level. The higher the difficulty level, the faster your snake moves", 1, black)
    text4 = LETTER_FONT.render("After you finish, your score will be stored into the leaderboards. Good Luck!", 1, black)
    screen.blit(text, (20,20))
    screen.blit(text2, (20,60))
    screen.blit(text3, (20,100))
    screen.blit(text4, (20,140))
    #difficulty choices
    choice = WORD_FONT.render("DIFFICULTY:",1,black)
    screen.blit(choice,(60, 200))
    #3 circles for 3 difficulty levels
    button1 = pygame.Rect(60,310,30,30)
    button2 = pygame.Rect(60,410,30,30)
    button3 = pygame.Rect(60,510,30,30)
    button4 = pygame.Rect(60,610,30,30)
    mx, my = pygame.mouse.get_pos()

    pygame.draw.rect(screen, green, button1)
    pygame.draw.rect(screen, yellow, button2)
    pygame.draw.rect(screen, red, button3)
    pygame.draw.rect(screen, black, button4)

    #easy difficulty
    easy=TITLE_FONT.render("1",1,green)
    screen.blit(easy,(100,300))
    choice1=TITLE_FONT.render("Easy",1,green)
    screen.blit(choice1,(160,300))

    #medium difficulty
    medium=TITLE_FONT.render("2",1,yellow)
    screen.blit(medium,(100,400))
    choice2=TITLE_FONT.render("Medium",1,yellow)
    screen.blit(choice2,(160,400))

    #hard difficulty
    hard=TITLE_FONT.render("3",1,red)
    screen.blit(hard,(100,500))
    choice3=TITLE_FONT.render("Hard",1,red)
    screen.blit(choice3,(160,500))

    quitmenu=TITLE_FONT.render("4",1,black)
    screen.blit(quitmenu,(100,600))
    choice4=TITLE_FONT.render("Quit",1,black)
    screen.blit(choice4,(160,600))

    pygame.display.update()
while run:
    menu()
    pygame.display.update()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
        sys.exit()
