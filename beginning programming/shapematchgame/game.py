from setup import *
import random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Shapes():
    def star(self):
        star = pygame.image.load('newstar.png')
        starrect = star.get_rect()
        starrect.center = (random.randint(100, 600), random.randint(100, 400))
        screen.blit(star, starrect)
        pygame.display.update()
    def rectangle(self):
        rectangle = pygame.image.load('rectangle.png')
        rectanglerect = rectangle.get_rect()
        rectanglerect.center = (random.randint(100, 600), random.randint(100, 400))
        screen.blit(rectangle, rectanglerect)
        pygame.display.update()
shapelist = Shapes()
class Cooldown():
    def __init__(self):
        self.cooltime = 1000
        self.oldtime = pygame.time.get_ticks()

    def randShape(self):
        my_list = [shapelist.star,shapelist.rectangle]
        time = pygame.time.get_ticks()
        if time - self.oldtime >= self.cooltime:
            self.oldtime = time
            screen.fill(white)
            random.choice(my_list)()
            print('Test2')

testing = Cooldown()
running = True
while (running):
    testing.randShape()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()
