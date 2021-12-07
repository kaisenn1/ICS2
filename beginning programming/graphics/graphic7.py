#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic7
#Description makes output window red

import pygame

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
    screen.fill((red))
    pygame.display.update()
pygame.quit()