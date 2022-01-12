#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel5
#Description configurable width band

import pygame

white = (255,255,255)
red = (255,0,0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

width = int(input('Band Width in Pixels:'))
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = 240
    screen.fill(white)
    for i in range(width):
        pygame.draw.line(screen,red,(320,x),(420,x))
        x += 1
    pygame.display.update()
pygame.quit()