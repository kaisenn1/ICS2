#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel1
#Description vertical red line

import pygame
import math

blue = (0, 0, 255)
white = (255, 255, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

width = int(input('Please Input Heart Width: '))

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
    pygame.draw.arc(screen,blue,(50 - width,50 - width / 2,50 + width,50 + width),p1,pp1)
    pygame.draw.arc(screen,blue,(100,50 - width / 2,50 + width,50 + width),p2,pp2)
    pygame.draw.line(screen,blue,(100,125 + width),(50 - width,75))
    pygame.draw.line(screen,blue,(100,125 + width),(150 + width,75))

    pygame.display.update()
pygame.quit()