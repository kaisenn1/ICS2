import asyncio
import pygame
import random

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


async def print_something():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('over')
            pygame.quit()


matching_shape = MatchingShape()

pygame.init()


async def run():
    print('test')
    previous_time = pygame.time.get_ticks()
    cooldown = 3000
    current_time = pygame.time.get_ticks()
    if current_time - previous_time >= cooldown:
        previous_time = current_time
        matching_shape.rand_shape()


loop = asyncio.get_event_loop()
loop.run_forever()