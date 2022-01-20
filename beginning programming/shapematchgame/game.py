from setup import *
import random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Cooldown():
    def __init__(self):
        self.cooltime = 2500
        self.oldtime = pygame.time.get_ticks()

    def Shapes(self):
        stime = pygame.time.get_ticks()
        star = pygame.image.load('newstar.png')
        rectangle = pygame.image.load('rectangle.png')
        shapes = [star, rectangle]
        image = shapes[random.randint(0, 1)]
        rect = image.get_rect()
        rect.center = (random.randint(100, 600), random.randint(100, 400))
        if stime - self.oldtime >= self.cooltime:
            self.oldtime = stime
            screen.blit(image, rect)
            pygame.display.update()
        return rect
    def randShape(self):
        if self.Shapes().collidepoint(pygame.mouse.get_pos()):
            screen.fill(white)
            pygame.display.update()
            print('collision')

testing = Cooldown()
running = True
screen.fill(white)
while (running):
    testing.randShape()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
