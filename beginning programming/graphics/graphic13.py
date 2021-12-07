#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic1
#Description creates 8 vertical stripes, asks for three colours, alternates stripe colour between three inputted colours
import pygame
from pygame.locals import *

black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

print('Choose three colours from the below list to set strip colours')
print('Black, Gray, White, Red, Green, Blue, Yellow, Cyan, Magenta')
colour = input('Input first colour name: ')
colour2 = input('Input second colour name: ')
colour3 = input('Input third colour name: ')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, colour,(0, 0,640,480))
    pygame.draw.rect(screen, colour2,(80, 0,640,480))
    pygame.draw.rect(screen, colour3,(160, 0,640,480))
    pygame.draw.rect(screen, colour,(240, 0,640,480))
    pygame.draw.rect(screen, colour2,(320, 0,640,480))
    pygame.draw.rect(screen, colour3,(400, 0,640,480))
    pygame.draw.rect(screen, colour,(480, 0,640,480))
    pygame.draw.rect(screen, colour2,(560, 0,640,480))
    pygame.display.update()
pygame.quit()