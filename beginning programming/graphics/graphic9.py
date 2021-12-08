#Name Kaisen
#Date Novemeber 26, 2021
#Title graphic9
#Description asks user for colour, name, and coordinates. sets background colour, and places name at inputted coordinates

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

n = input('Please enter your name: ')
r = int(input('Please enter row number: '))
c = int(input('Please enter column number: '))
print('Choose a colour from the below list to set background colour')
print('Black, Gray, White, Red, Green, Blue, Yellow, Cyan, Magenta')
colour = input('Input a colour name: ')

pygame.init()
sysfont = pygame.font.get_default_font()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

font = pygame.font.SysFont(sysfont, 50)
text = font.render(n, 1, black)
center = text.get_rect(center=(c, r))
screen.fill((colour))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text, center)
    pygame.display.update()
pygame.quit()