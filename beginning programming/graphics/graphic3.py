#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic3
#Description draws 10 stars vertically down the center of the screen using a for loop

import pygame

SCREEN_WIDTH   = 640
SCREEN_HEIGHT  = 480

white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
star = pygame.image.load('star.png')
smallStar = pygame.transform.scale(star,(50,50))

running = True
while (running):
    event = pygame.event.poll()
    screen.fill(white)
    x = 0
    for i in range(10):
        screen.blit(smallStar, (300, x))
        x += 48
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()