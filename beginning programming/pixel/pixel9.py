#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel9
#Description triangle

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
    pygame.draw.polygon(screen, purple, ((50, 100), (100, 50), (150, 100))) #my border is purple
    pygame.display.update()
pygame.quit()