#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic1
# Description prints kaisen in center of screen

import pygame
from pygame.locals import *

red = (255, 0, 0)
green = (0, 255, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, red,(0, 0,160,480))
    pygame.draw.rect(screen, green,(160, 0,160,480))
    pygame.draw.rect(screen, red,(320, 0,160,480))
    pygame.draw.rect(screen, green,(480, 0,160,480))
    pygame.display.update()
pygame.quit()