__author__ = "Karthikeyan S"

import sys
import pygame
import random

pygame.init()

scr_size = (width,height) = (600,600)

black = (0,0,0)
white = (255,255,255)
blue = (0,0,128)
red = (255,0,0)

SPEED = 2
limit = 1
eggs_lost = 0
score = 0
catch = False
stone_limit = 0

background_colour = black
basket_size = 30
basket_pos = [width/2, height - basket_size]
myFont = pygame.font.SysFont("monospace", 20)

egg_size = 10
egg_pos = [random.randint(0,width-egg_size), 0]
egg_list = [egg_pos]

stone_size = 10
stone_pos = [random.randint(0,width-stone_size), 0]
stone_list = [stone_pos]

screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption("Catch the egg")
clock = pygame.time.Clock()

gameOver = False
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
            if (e_y == b_y):
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


while not gameOver:
    screen.fill(background_colour)
    print(SPEED)
    print(limit)
    
    #Increasing difficulty based on score
    if score >= 5:
        stone_limit = 1
        limit = 2
        SPEED = 5
    elif score >= 10:
        stone_limit = 3
        limit = 3
        SPEED = 7

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
    delay = random.random()
    if len(egg_list) < limit:
        x_pos = random.randint(0,width-egg_size)
        y_pos = 0
        egg_list.append([x_pos, y_pos])    
    #Drawing the eggs
    for egg_pos in egg_list:
        pygame.draw.rect(screen, white, (egg_pos[0], egg_pos[1], egg_size, egg_size))
        
        
    #Dropping the eggs
    for index, egg_pos in enumerate(egg_list):
        if egg_pos[1] >= 0 and egg_pos[1] < height:
            egg_pos[1] += SPEED
        else:
            egg_list.pop(index)
            eggs_lost += 1

    if catch_check(egg_list, basket_pos):
	    score += 1

    delay = random.random()
    if len(stone_list) < stone_limit:
        x_pos = random.randint(0,width-egg_size)
        y_pos = 0
        stone_list.append([x_pos, y_pos])    
    #Drawing the stones
    for stone_pos in stone_list:
        pygame.draw.rect(screen, red, (stone_pos[0], stone_pos[1], stone_size, stone_size))
            
    #Dropping the stones
    for index, stone_pos in enumerate(stone_list):
        if stone_pos[1] >= 0 and stone_pos[1] < height:
            stone_pos[1] += SPEED
        else:
            stone_list.pop(index)

    if stone_catch_check(stone_list, basket_pos):
        score -=1
        eggs_lost += 1
	   
    text = "Score : " + str(score)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-175, height-600))    
    
    text = "Eggs Lost : " + str(eggs_lost)
    label = myFont.render(text, 1, white)
    screen.blit(label, (width-175, height-580))    
    pygame.draw.rect(screen, red, (basket_pos[0], basket_pos[1], basket_size, basket_size))

    if eggs_lost >= 10:
        gameOver = True
    pygame.display.update()
    

