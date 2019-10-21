__author__ = "Karthikeyan S"

import sys
import pygame
import random
from random import randint
from itertools import cycle

pygame.init()
pygame.mixer.pre_init(44100,-16,1,512)
pygame.mixer.init()

scr_size = (width,height) = (800,600)

black = (0,0,0)
white = (255,255,255)
steel_blue = (70,130,180)
brown = (153,76,0)
basket_border = (204,102,0)
yellow = (255, 255, 0)
green = (0,128,0)
red = (128,0,0)

SPEED = 2
limit = 1
eggs_lost = 0
score = 0
catch = False
stone_limit = 0
delay = 1000

milli_seconds_unit = 0
milli_seconds_tens = 0
milli_seconds_hundreds = 0

seconds_unit = 0
seconds_tens = 0

minutes_unit = 0
minutes_tens = 0

level_up_1_music_count = 0
level_up_2_music_count = 0

background_colour = steel_blue
basket_size = 20
basket_pos = [width/2, height - basket_size]
myFont = pygame.font.SysFont("monospace", 20)

egg_size = 10
egg_pos = [random.randint(0,width-egg_size), 0]
egg_list = [egg_pos]

pi = 3.14
stone_size = 5
stone_pos = [random.randint(0,width-stone_size), 0]
stone_list = [stone_pos]

screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption("Catch the egg")

gameOver = False
gameStart = False
gameQuit = False
BLINK_EVENT = pygame.USEREVENT + 0
clock = pygame.time.Clock()

def drawSun():
    pygame.draw.circle(screen, yellow,(700,100),25)
    
def drawHillFarmHouse():
    pygame.draw.ellipse(screen, green, (20, 500, 500, 550))
    pygame.draw.rect(screen, red, (230, 470 , 40, 35))
    pygame.draw.polygon(screen, black, ((225, 470) , (275, 470) , (250, 430)) )

def drawCloud():
    #cloud 1 
    size = 35
    xOffset = 13
    yOffset = 30
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 67
    xOffset = -9 
    yOffset = 18
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 41
    xOffset = -36
    yOffset = 19
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 66
    xOffset = -31 
    yOffset = -13
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 61
    xOffset = -18 
    yOffset = -14
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 33
    xOffset = 39 
    yOffset = -2
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 52
    xOffset = -35 
    yOffset = -12
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 50
    xOffset = -29 
    yOffset = 3
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 20
    xOffset = -22 
    yOffset = 28
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 23
    xOffset = -33 
    yOffset = -7
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 37
    xOffset = 20 
    yOffset = 19
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 35
    xOffset = 9 
    yOffset = 5
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 50
    xOffset = -31 
    yOffset = -28
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 54
    xOffset = 24 
    yOffset = 11
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 37
    xOffset = -13 
    yOffset = 5
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    #cloud 2
    size = 45
    xOffset = 538 
    yOffset = 148
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 20
    xOffset = 542 
    yOffset = 105
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 24
    xOffset = 505
    yOffset = 127
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 60
    xOffset = 511
    yOffset = 132
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 25
    xOffset = 534 
    yOffset = 114
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 48
    xOffset = 520 
    yOffset = 127
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 58
    xOffset = 536 
    yOffset = 102
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 42
    xOffset = 532 
    yOffset = 124
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 50
    xOffset = 538 
    yOffset = 101
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 42
    xOffset = 533 
    yOffset = 117
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 23
    xOffset = 503 
    yOffset = 135
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 53
    xOffset = 528 
    yOffset = 108
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 48
    xOffset = 528 
    yOffset = 111
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 38
    xOffset = 510 
    yOffset = 136
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

    size = 64
    xOffset = 502 
    yOffset = 129
    pygame.draw.ellipse(screen,white,(100+xOffset,100+yOffset,size, size + 2))

def catch_check(egg_list, basket_pos):
	for egg_pos in egg_list:
		if catch_detect(egg_pos, basket_pos):
			return True
	return False

def catch_detect(egg_pos, basket_pos):
    for index, egg_pos in enumerate(egg_list):
        b_x = basket_pos[0]
        b_y = basket_pos[1]

        e_x = egg_pos[0]
        e_y = egg_pos[1]

        if (e_x >= b_x and e_x <= b_x + basket_size):
            if (e_y <= b_y + 0.1 and e_y >= b_y - 0.1):
                egg_list.pop(index)
                return True
        return False
    
def stone_catch_check(stone_list, basket_pos):
    for stone_pos in stone_list:
	    if stone_collide_detect(stone_pos, basket_pos):
		    return True
    return False

def stone_collide_detect(stone_pos, basket_pos):
    for index, stone_pos in enumerate(stone_list):
        b_x = basket_pos[0]
        b_y = basket_pos[1]

        s_x = stone_pos[0]
        s_y = stone_pos[1]

        if ((s_x >= b_x and s_x <= b_x + basket_size) or (b_x >= s_x and b_x < (s_x+stone_size))):
            if (s_y >= b_y and s_y < (b_y + basket_size)) or (b_y >= s_y and b_y < (s_y+stone_size)):
                stone_list.pop(index)
                return True
        return False

pygame.mixer.music.load("Electronic-beat.mp3")
pygame.mixer.music.play()

file1 = open("HighScore.txt","r")
highScoreString = file1.read()
highScore = int(highScoreString) 
file1.close()

#Welcome screen
screen.fill(black)
screen_rect = screen.get_rect()
welcome_text = myFont.render('Interactive Computer Graphics Assignment - CED16I015', 1,pygame.Color('green3'))
screen.blit(welcome_text,(width-700, height-400))
on_blink_surface = myFont.render('Press Any Key To Start', 1, pygame.Color('green3'))
blink_rect = on_blink_surface.get_rect()
blink_rect.center = screen_rect.center
off_text_surface = pygame.Surface(blink_rect.size)
blink_surfaces = cycle([on_blink_surface, off_text_surface])
blink_surface = next(blink_surfaces)
pygame.time.set_timer(BLINK_EVENT, 1000)

while not gameStart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            gameStart = True
                
        if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)

    screen.blit(blink_surface, blink_rect)
    pygame.display.update()

screen.fill(background_colour)   
while not gameOver:
    clock.tick(60)
    screen.fill(background_colour)    
    drawCloud()
    drawSun()
    drawHillFarmHouse()
    #Increasing difficulty based on score
    if score >= 1:
        stone_limit = 1
        limit = 2
        SPEED = 2
        #basket_pos[1] = height - basket_size -10
        level_up_1_music_count += 1
        if(level_up_1_music_count == 1):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('smw_power-up.wav'))
    
    elif score >= 10:
        stone_limit = 2
        limit = 2
        SPEED = 3
        #basket_pos[1] = height - basket_size -20
        level_up_2_music_count += 1
        if(level_up_2_music_count == 1):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('smw_power-up.wav'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = basket_pos[0]
            y = basket_pos[1]
            if event.key == pygame.K_LEFT:
                #Warping from extreme left to extreme right
                if x == 0:
                    x = width
                else: 
                    x-=10
            if event.key == pygame.K_RIGHT:
                #Warping from extreme right to extreme left
                if x == width:
                    x = 0
                else:
                    x+=10
            basket_pos = [x,y]

    #Choosing drop location of eggs
    if len(egg_list) < limit:
        x_pos = random.randint(0,width-egg_size)
        y_pos = 0
        egg_list.append([x_pos, y_pos])

    #Drawing the eggs
    for egg_pos in egg_list:
        pygame.draw.ellipse(screen, white, (egg_pos[0], egg_pos[1], egg_size, egg_size + 2))
  
    #Dropping the eggs
    for index, egg_pos in enumerate(egg_list):
        if index == 0:
            egg_speed = SPEED
        else:
            egg_speed = SPEED - 1    
        if egg_pos[1] >= 0 and egg_pos[1] < height:
                egg_pos[1] += egg_speed
        else:
            egg_list.pop(index)
            eggs_lost += 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('smw_bubble_pop.wav'))

    if catch_check(egg_list, basket_pos):
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('smw_coin.wav'))
        score += 1

    if len(stone_list) < stone_limit:
        x_pos = random.randint(0,width-egg_size)
        y_pos = 0
        stone_list.append([x_pos, y_pos])    
    #Drawing the stones
    for stone_pos in stone_list:
        pygame.draw.circle(screen, black, (stone_pos[0], stone_pos[1]), stone_size)
            
    #Dropping the stones
    for index, stone_pos in enumerate(stone_list):
        if stone_pos[1] >= 0 and stone_pos[1] < height:
            stone_pos[1] += SPEED
        else:
            stone_list.pop(index)

    if stone_catch_check(stone_list, basket_pos):
        score -= 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('smw_bubble_pop.wav'))
        eggs_lost += 1
	
    #Count up timer
    if milli_seconds_unit < 9:
        if milli_seconds_tens < 9:
            milli_seconds_unit += 1
    
    if milli_seconds_unit == 9 and milli_seconds_tens < 9:
        milli_seconds_unit = 0
        milli_seconds_tens += 1

    elif milli_seconds_tens == 9 and milli_seconds_hundreds < 1:
        milli_seconds_tens = 0
        milli_seconds_hundreds += 1

    if milli_seconds_hundreds == 1:
        if seconds_unit < 9:
            seconds_unit += 1
            milli_seconds_hundreds = 0
        else:
                seconds_unit = 0
                seconds_tens += 1
                milli_seconds_hundreds = 0

    if seconds_tens == 6:
        if minutes_unit < 9:
            minutes_unit += 1
            seconds_tens = 0
        else:
            minutes_unit = 0
            minutes_tens += 1
            seconds_tens = 0

    if minutes_tens == 6:
        seconds_unit = 0
        seconds_tens = 0
        minutes_unit = 0
        minutes_tens = 0
        game_over_text = myFont.render('Game Over!!! Score : ' + str(score), 1,white)
        screen.blit(game_over_text,(width-520, height-400))
        on_over_blink_surface = myFont.render('Press q to Quit', 1, white)
        blink_over_rect = on_over_blink_surface.get_rect()
        blink_over_rect.center = screen_rect.center
        off_text_surface = pygame.Surface(blink_over_rect.size)
        off_text_surface.fill(steel_blue)
        blink_surfaces = cycle([on_over_blink_surface, off_text_surface])
        blink_surface = next(blink_surfaces)
        pygame.time.set_timer(END_BLINK_EVENT, 1000)
    
        while not gameQuit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_q):
                        gameQuit = True
                    if event.type == END_BLINK_EVENT:
                        blink_surface = next(blink_surfaces)

            screen.blit(blink_surface, blink_over_rect)
            pygame.display.update() 
    
    text = "Time Taken : " + str(minutes_tens) + str(minutes_unit) + ":" +  str(seconds_tens) + str(seconds_unit)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-225, height-600))

    text = "Score : " + str(score)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-175, height-580))    
    
    text = "High Score : " + str(highScore)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-175, height-540))

    text = "Eggs Lost : " + str(eggs_lost)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-175, height-560)) 

    pygame.draw.circle(screen, brown, (int(basket_pos[0] + 15), int(basket_pos[1])), 10)
    pygame.draw.circle(screen, steel_blue, (int(basket_pos[0] + 15), int(basket_pos[1])), 5)   
    pygame.draw.rect(screen, brown, (basket_pos[0], basket_pos[1], basket_size + 10, basket_size))
    pygame.draw.line(screen, basket_border, (basket_pos[0] ,basket_pos[1] + 6.67), (basket_pos[0] + basket_size + 10 ,basket_pos[1] + 6.67 ) , 1)
    pygame.draw.line(screen, basket_border, (basket_pos[0] ,basket_pos[1] + 13.34), (basket_pos[0] + basket_size + 10 ,basket_pos[1] + 13.34 ) , 1)
    pygame.draw.line(screen, basket_border, (basket_pos[0] + 10 ,basket_pos[1]), (basket_pos[0] + 10 ,basket_pos[1] + 20 ) , 1)
    pygame.draw.line(screen, basket_border, (basket_pos[0] + 20 ,basket_pos[1]), (basket_pos[0] + 20 ,basket_pos[1] + 20 ) , 1)
    
    if eggs_lost >= 1000:
        gameOver = True
    pygame.display.update()

END_BLINK_EVENT = pygame.USEREVENT + 0
#End screen
screen.fill(steel_blue)
screen_rect = screen.get_rect()
if score > highScore:
    game_over_text = myFont.render('New High Score!!! Score : ' + str(score), 1,white)
    file1 = open("HighScore.txt","w")
    file1.write(str(score))
else:
    game_over_text = myFont.render('Game Over!!! Score : ' + str(score), 1,white)
screen.blit(game_over_text,(width-520, height-400))
on_over_blink_surface = myFont.render('Press q to Quit', 1, white)
blink_over_rect = on_over_blink_surface.get_rect()
blink_over_rect.center = screen_rect.center
off_text_surface = pygame.Surface(blink_over_rect.size)
off_text_surface.fill(steel_blue)
blink_surfaces = cycle([on_over_blink_surface, off_text_surface])
blink_surface = next(blink_surfaces)
pygame.time.set_timer(END_BLINK_EVENT, 1000)

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_q):
                gameQuit = True
        if event.type == END_BLINK_EVENT:
            blink_surface = next(blink_surfaces)

        screen.blit(blink_surface, blink_over_rect)
        pygame.display.update() 
        
if gameQuit == True:
    sys.exit()    

