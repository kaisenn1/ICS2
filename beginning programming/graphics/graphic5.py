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
centre_coord = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
star = pygame.image.load('star.png')
smallStar = pygame.transform.scale(star,(50,50))

startX = int(input('Please enter starting X coordinate: '))
startY = int(input('Please enter starting Y coordinate: '))

running = True
while (running):
    event = pygame.event.poll()
    screen.fill(white)
    x = startX
    y = startY
    for i in range(10):
        screen.blit(smallStar, (y, x))
        x += 48
        y += 64
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()