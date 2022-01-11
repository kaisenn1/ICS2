#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel1
#Description bored face

import pygame

white = (255,255,255)
black = (0, 0, 0)

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
    pygame.draw.rect(screen, black,(200, 200,5,5))
    pygame.draw.rect(screen, black,(435, 200,5,5))
    pygame.draw.line(screen,black,(220,320),(420,320))
    pygame.display.update()
pygame.quit()