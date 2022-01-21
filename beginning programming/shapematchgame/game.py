from setup import *
import random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
star = pygame.image.load('newstar.png')
rectangle = pygame.image.load('rectangle.png')
shapes = [rectangle, star]

class Cooldown():
    def __init__(self):
        self.cooltime = 2000
        self.cooltime1 = 250
        self.copy = star.get_rect()
        self.oldtime = pygame.time.get_ticks()
    def random1(self):
        num = (random.randint(100, 600), random.randint(100, 400))
        return num


    def randShape(self):
        image = shapes[random.randint(0, 1)]
        rect = image.get_rect()
        screen.fill(white)
        pygame.display.update()
        rect.center = self.random1()
        screen.blit(image, rect)
        pygame.display.update()
        self.copy = rect.copy()
        return self.copy


    def test(self):
        x = self.copy
        if x.collidepoint(pygame.mouse.get_pos()):
            print('ye')
testing = Cooldown()
running = True
screen.fill(white)
cooltime = 1000
oldtime = pygame.time.get_ticks()
x = None
while (running):
    time = pygame.time.get_ticks()
    if time - oldtime >= cooltime:
        oldtime = time
        if testing.randShape().collidepoint(pygame.mouse.get_pos()):
            print('ye')
    testing.test()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()