#Name Kaisen
#Date Novemeber 26, 2021
#Title pixel6
#Description configurable band

import pygame

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

width = int(input('Band Width in Pixels:'))
length = int(input('Band Length in Pixels:'))
print('--- Colour from Below List ---')
print('Black, Gray, White, Red, Green, Blue, Yellow, Cyan, Magenta')
colour = input('Colour Name: ')
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
        pygame.draw.line(screen,colour,(320,x),(320 + length,x))
        x += 1

    pygame.display.update()
pygame.quit()