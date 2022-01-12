#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel1
#Description vertical red line

import pygame

gray = (127, 127, 127)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)



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
    pygame.draw.circle(screen,blue,(50,50),25,5)
    pygame.draw.circle(screen,red,(50,50),20,5)
    pygame.draw.circle(screen,yellow,(50,50),15,5)
    pygame.draw.circle(screen,green,(50,50),10,5)
    pygame.draw.circle(screen,magenta,(50,50),5,5)
    pygame.draw.rect(screen, gray, (47.5,75,5,50))
    pygame.display.update()
pygame.quit()