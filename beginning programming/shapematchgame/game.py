from setup import *
import random

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
star = pygame.image.load('newstar.png')
rectangle = pygame.image.load('rectangle.png')
shapes = [rectangle, star]

class Cooldown():

    def __init__(self):
        self.score = 0

    def randShape(self):
        image = shapes[random.randint(0, 1)]
        rect = image.get_rect()
        screen.fill(white)
        pygame.display.update()
        rect.center = (random.randint(100, 600), random.randint(100, 400))
        screen.blit(image, rect)
        pygame.display.update()
        self.shapecopy = rect.copy()
        return self.shapecopy

    def clicktest(self):
        collider = self.shapecopy
        for event in pygame.event.get():
            if collider.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                self.score += 1
                screen.fill(white)
                self.scoreboard()
                pygame.display.update()
    def scoreboard(self):
        sysfont = pygame.font.get_default_font()
        font = pygame.font.SysFont(sysfont, 50)
        text = font.render('Score:'+str(self.score), 1, black)
        center = text.get_rect(center=(75,20))
        screen.blit(text,center)
testing = Cooldown()

screen.fill(white)
cooltime = 3000
oldtime = pygame.time.get_ticks()
running = True
pygame.init()
p = 0
while (running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = pygame.time.get_ticks()
    if time - oldtime >= cooltime:
        oldtime = time
        testing.randShape()
        p = 1
    if p == 1:
        testing.clicktest()



pygame.quit()