# Name Kaisen
# Date Novemeber 26, 2021
# Title pixel12
# Description prints kaisen in center of screen inside a rectangle

from setup import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
star = pygame.image.load('newstar.png')

starrect = star.get_rect()
running = True
while running:
    screen.fill(white)
    screen.blit(star, starrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mousepos = event.pos
            if pygame.mouse.get_pressed()[0] and starrect.collidepoint(event.pos):
                starrect.center = event.pos
                print(mousepos)
    pygame.display.update()
pygame.quit()
