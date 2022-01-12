#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel1
#Description vertical red line

import pygame
import math

white = (255, 255, 255)
blue = (0, 0, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

p1 = math.radians(20)
pp1 = math.radians(180)
p2 = math.radians(1)
pp2 = math.radians(160)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.arc(screen,blue,(50,50,50,50),p1,pp1)
    pygame.draw.arc(screen,blue,(100,50,50,50),p2,pp2)
    pygame.draw.line(screen,blue,(100,125),(50,75))
    pygame.draw.line(screen,blue,(100,125),(150,75))

    pygame.display.update()
pygame.quit()