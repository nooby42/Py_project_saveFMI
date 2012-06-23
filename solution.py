import pygame, sys, Enemy
from pygame.locals import *

pygame.font.init()
running = 1
pressed_down=False
strike=False
time=0
hits=0

screen = pygame.display.set_mode((600, 600));
enemy_image = pygame.image.load("KS_H_SM.bmp").convert()
enemy_image.set_colorkey((180,180,180))
cursor = pygame.image.load("Cursor.bmp").convert()
cursor.set_colorkey((180,180,180))
enemy_dead = pygame.image.load("KS_SAD_SM.bmp").convert()
enemy_dead.set_colorkey((180,180,180))
background = pygame.image.load("Field.jpg").convert()
bang = pygame.image.load("Bang!.bmp").convert()
bang.set_colorkey((255,255,255))
clock=pygame.time.Clock()
enemy1= Enemy.Enemy(160,140,1000,3000,False,enemy_image)
enemy2= Enemy.Enemy(351,140,2500,4500,False,enemy_image)
enemy3= Enemy.Enemy(355,401,4000,6500,False,enemy_image)
enemy4= Enemy.Enemy(200,401,6500,8000,False,enemy_image)
enemy5= Enemy.Enemy(258,275,8500,10500,False,enemy_image)
enemy6= Enemy.Enemy(460,527,10000,12000,False,enemy_image)
enemy7= Enemy.Enemy(45,528,12500,13500,False,enemy_image)
enemy8= Enemy.Enemy(255,530,13000,15000,False,enemy_image)
enemy9= Enemy.Enemy(450,94,14500,16500,False,enemy_image)
enemy10= Enemy.Enemy(62,94,16000,18000,False,enemy_image)
enemy11= Enemy.Enemy(242,94,18800,20000,False,enemy_image)
pygame.mouse.set_visible(0)
enemies=[enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11]


def strike_checker(mouse_click_coordinates, x_of_image, y_of_image):
    if (mouse_click_coordinates[0] > x_of_image and mouse_click_coordinates[0] < x_of_image+50 and 
        mouse_click_coordinates[1] > y_of_image and mouse_click_coordinates[1] < y_of_image + 70):
        return True
        
def clear_screen():
    screen.blit(background, (0,0))
    
def paint_enemy(enemy_image,x,y):
    screen.blit(enemy_image, (x,y))
    
    
def time_checker(time,born_time,death_time):
    if(time > born_time and time < death_time):
        return True
      
while running:
    if pygame.event.peek():
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
            
        screen.fill((0, 0, 0))
        clear_screen()
       
        if (event.type == MOUSEBUTTONDOWN):
            cords=pygame.mouse.get_pos()
            for enemy in enemies:
                if(time_checker(time,enemy.born,enemy.died) and not enemy.hit):
                    enemy.hit=strike_checker(cords, enemy.x, enemy.y)
                    if(enemy.hit):
                        enemy.image=bang
                        hits=hits+1
            
        if (event.type == MOUSEBUTTONUP):
            pressed_down = False
            for enemy in enemies:
                if enemy.hit:
                    enemy.image=enemy_dead
                
        
    time=time+clock.get_time();
    if(time > 20001):
        time=0
        for enemy in enemies:
            enemy.hit=False
            enemy.image=enemy_image
            
    for enemy in enemies: 
        if(time_checker(time,enemy.born,enemy.died)):
            paint_enemy(enemy.image,enemy.x,enemy.y)
        if(time >= enemy.died):
            clear_screen()
            
    font = pygame.font.Font('Fonter.ttf', 25)
    printer='tohki: ' +str(hits)
    text = font.render(printer, True, (255,255, 255), (159, 182, 205))
    screen.blit(text, (5,5))
    cursor.set_colorkey((180,180,180))
    cordss=pygame.mouse.get_pos()
    screen.blit(cursor,(cordss[0],cordss[1]))
    clock.tick(60) 
    pygame.display.update()