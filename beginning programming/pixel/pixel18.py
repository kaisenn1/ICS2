#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel18
#Description superpepsi cylinder

import pygame
import math

black = (0, 0, 0)
white = (255, 255, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

p1 = math.radians(180)
pp1 = math.radians(0)

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(sysfont, 25)
text = font.render('SuperPepsi', 1, black)
center = text.get_rect(center=(150, 200))

screen.fill((white))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.ellipse(screen,black,(100,75,100,50),1)
    pygame.draw.arc(screen,black,(100,275,100,50),p1,pp1)
    pygame.draw.line(screen,black,(100,100),(100 ,300))
    pygame.draw.line(screen,black,(200,100),(200 ,300))
    screen.blit(text, center)
    pygame.display.update()
pygame.quit()