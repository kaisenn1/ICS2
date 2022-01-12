#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel19
#Description watermelon

import pygame
import math

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

p1 = math.radians(270)
pp1 = math.radians(0)

screen.fill((white))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.arc(screen,green,(100,275,100,100),p1,pp1,5)
    pygame.draw.arc(screen,red,(100,275,95,95),p1,pp1,50)
    pygame.display.update()
pygame.quit()