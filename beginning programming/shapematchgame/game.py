from setup import *
import random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
star = pygame.image.load('newstar.png')
rectangle = pygame.image.load('rectangle.png')
shapes = [rectangle, star]
'''test'''
class Cooldown():
    def __init__(self):
        self.cooltime = 5000
        self.cooltime1 = 250
        self.oldtime = pygame.time.get_ticks()
    def random1(self):
        num = (random.randint(100, 600), random.randint(100, 400))
        return num

    score1 = 0
    def randShape(self):
        time = pygame.time.get_ticks()
        image = shapes[random.randint(0, 1)]
        rect = image.get_rect()
        copy = rect.copy()
        copy.center = self.random1()
        if time - self.oldtime >= self.cooltime:
            self.oldtime = time
            screen.fill(white)
            pygame.display.update()
            rect.center = self.random1()
            screen.blit(image, rect)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.score1 += 1
                print(self.score1)
        if copy.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            screen.fill(white)
            pygame.display.update()
        return image

    def otherShape(self, image):
        time = pygame.time.get_ticks()
        shapes.remove(image)
        image2 = shapes[0]
        if time - self.oldtime >= self.cooltime1:
            self.oldtime = time
            rect = image2.get_rect()
            pygame.display.update()
            rect.center = self.random1()
            screen.blit(image2, rect)
            pygame.display.update()



testing = Cooldown()
running = True
screen.fill(white)

while (running):
    testing.otherShape(testing.randShape())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()