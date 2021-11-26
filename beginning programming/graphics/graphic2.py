#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic2
# Description prints inputted name on inputted row

import pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

n = input('Please enter your name: ')
r = int(input('Please enter row number: '))
pygame.init()
sysfont = pygame.font.get_default_font()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


font = pygame.font.SysFont(sysfont, 50)
text = font.render(n, 1, black)
center = text.get_rect(center=(SCREEN_WIDTH/2, r))
screen.fill((white))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text, center)
    pygame.display.update()
pygame.quit()