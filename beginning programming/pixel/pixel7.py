#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel7
#Description vertical red line

import pygame

white = (255,255,255)
red = (255,0,0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.line(screen,red,(0,0),(100,0))
    pygame.draw.line(screen,red,(0,20),(100,20))
    pygame.draw.line(screen,red,(0,0),(0,20))
    pygame.draw.line(screen,red,(100,0),(100,20))
    pygame.display.update()
pygame.quit()