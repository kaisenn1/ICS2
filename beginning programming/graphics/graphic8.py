#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic7
# Description changes background colour to red

import pygame
import time

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

print('Choose a colour from the below list to set background colour')
print('Black, Gray, White, Red, Green, Blue, Yellow, Cyan, Magenta')
time.sleep(0.5)
colour = input('Input a colour name: ')
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((colour))
    pygame.display.update()
pygame.quit()