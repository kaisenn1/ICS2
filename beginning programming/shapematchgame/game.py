import random
import threading
import pygame

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((640, 480))
star = pygame.image.load('star.png')
rectangle = pygame.image.load('rectangle.png')
shapes = [rectangle, star]


class MatchingShape:

    def __init__(self):
        self.rect = None
        self.score = 0

    def rand_shape(self):
        screen.fill(white)
        image = shapes[random.randint(0, 1)]
        self.rect = image.get_rect()
        self.rect.center = (random.randint(100, 600), random.randint(100, 400))
        screen.blit(image, self.rect)
        pygame.display.update()

    def collision_test(self):
        for event in pygame.event.get():
            if self.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                self.score += 1
                screen.fill(white)
                scoreboard()
                pygame.display.update()


matching_shape = MatchingShape()


def scoreboard():
    system_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(system_font, 50)
    text = font.render('Score: ' + str(matching_shape.score), 1, black)
    center = text.get_rect(center=(75, 20))
    screen.blit(text, center)


previous_time = pygame.time.get_ticks()
cooldown = 3000
activated = 0

pygame.init()

Running = True
while Running:
    current_time = pygame.time.get_ticks()

    if current_time - previous_time >= cooldown:
        previous_time = current_time
        matching_shape.rand_shape()
        activated = 1
    if activated == 1:
        matching_shape.collision_test()
pygame.quit()
