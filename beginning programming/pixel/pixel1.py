#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel1
#Description red line 100 pixels long, fron 15,10

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
    pygame.draw.line(screen,red,(15,10),(115,10))
    pygame.display.update()
pygame.quit()