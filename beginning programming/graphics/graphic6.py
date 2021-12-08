#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic6
#Description draws 10 stars vertically across the screen, user chooses starting point, if star will touch edge, program quits

import pygame
import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
star = pygame.image.load('star.png')
smallStar = pygame.transform.scale(star,(50,50))

startX = int(input('Please enter starting X coordinate: '))
startY = int(input('Please enter starting Y coordinate: '))

time.sleep(1)

running = True
while (running):
    event = pygame.event.poll()
    screen.fill(white)
    x = startX
    y = startY
    for i in range(10):
        if x > 640 or y > 480:
            print('Object will be out of bounds, quitting')
            pygame.quit()

        time.sleep(0.5)
        screen.blit(smallStar, (y, x))
        x += 48
        y += 64
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()