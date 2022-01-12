#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic1
#Description prints kaisen in center of screen

import pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
purple = (221,160,221)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
sysfont = pygame.font.get_default_font()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

font = pygame.font.SysFont(sysfont, 50)
text = font.render('Kaisen', 1, black)
center = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
screen.fill((white))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, purple, center)
    screen.blit(text, center)
    pygame.display.update()
pygame.quit()