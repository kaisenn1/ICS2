#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic2
# Description prints inputted name on inputted row

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

    y = 0
    x = 0

    for i in range(10):
        screen.blit(smallStar, (y, x))
        x += 48
        y += 64
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()