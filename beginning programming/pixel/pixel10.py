#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel10
#Description arrow

import pygame

white = (255,255,255)
purple = (221,160,221)


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
    pygame.draw.rect(screen, purple,(50, 50,50,25))
    pygame.draw.polygon(screen, purple, ((100, 25), (100, 100), (150, 62)))
    pygame.display.update()
pygame.quit()