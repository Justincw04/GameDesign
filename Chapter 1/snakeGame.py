import pygame
import time
import random
import sys
pygame.init()



b = 20
a = 20

#colors for later use
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 165, 0)
dgreen = (0, 100, 0)

RADIUS = 10
WIDTH = 1400
HEIGHT = 800
run = True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
#making fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
#menu with instruction list and difficulty selector
def menu():
    global click
    screen.fill(blue)
    text = TITLE_FONT.render("Let's Play Snake!", 1, black)

    #instructions
    text = LETTER_FONT.render("In this game, use your arrow keys to move the direction of your snake. Eat food to grow", 1, black)
    text2 = LETTER_FONT.render("longer and earn points. If you hit a wall or hit your own snake, you will lose", 1, black)
    text3 = LETTER_FONT.render("First, choose your difficulty level. The higher the difficulty level, the faster your snake moves", 1, black)
    text4 = LETTER_FONT.render("After you finish, your score will be stored into the leaderboards. Good Luck!", 1, black)
    #positioning of text
    screen.blit(text, (20,20))
    screen.blit(text2, (20,60))
    screen.blit(text3, (20,100))
    screen.blit(text4, (20,140))
    #difficulty choices
    choice = WORD_FONT.render("DIFFICULTY:",1,black)
    screen.blit(choice,(60, 200))
    #4 rectangles for 3 difficulty levels and 1 quit button
    button1 = pygame.Rect(60,310,30,30)
    button2 = pygame.Rect(60,410,30,30)
    button3 = pygame.Rect(60,510,30,30)
    button4 = pygame.Rect(60,610,30,30)
    #finding position of mouse
    mx, my = pygame.mouse.get_pos()
    #4 rectangles, each the same size but different color and position
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

    #quit button
    quitmenu=TITLE_FONT.render("4",1,black)
    screen.blit(quitmenu,(100,600))
    choice4=TITLE_FONT.render("Quit",1,black)
    screen.blit(choice4,(160,600))

    pygame.display.update()

    event = pygame.event.poll()

    #detect if mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            click = True
    #detect if mouse position collides with position of rectangles,
    #rectangles correspond with game function of difficulty
    if button1.collidepoint((mx,my)):
        if click:
            gameLoopEasy()
            pass
    if button2.collidepoint((mx,my)):
        if click:
            gameLoopMedium()
            pass
    if button3.collidepoint((mx,my)):
        if click:
            gameLoopHard()
            pass
    if button4.collidepoint((mx,my)):
        if click:
            pygame.quit()
    #other options to quit besides clicking the button
    keyBoardKey = pygame.key.get_pressed()
    if keyBoardKey[pygame.K_ESCAPE]:
        pygame.quit()
    if event.type == pygame.QUIT:
        run=False
        sys.exit()
    click = False



pygame.time.delay(5000)
snake_block = 10

#other fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#function for score number
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])


#function for snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

#easy difficulty/low speed
def gameLoopEasy():
    #speed of snake
    snake_speed = 15
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #coordinates of food
    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            #lose message
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            #2 options: quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run = True
                        while run:
                            menu()
                            pygame.display.update()
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                run = False
                                sys.exit()

        #commands to make snake move with keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(dgreen)
        #drawing everything
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        #scores
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

#same code but faster speed for medium difficulty
def gameLoopMedium():
    snake_speed = 20
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run = True
                        while run:
                            menu()
                            pygame.display.update()
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                run = False
                                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(orange)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
#same code but for faster hard difficulty
def gameLoopHard():
    snake_speed = 25
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run = True
                        while run:
                            menu()
                            pygame.display.update()
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                run = False
                                sys.exit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(red)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
#code to make game run
while run:
    menu()
    pygame.display.update()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
        sys.exit()
