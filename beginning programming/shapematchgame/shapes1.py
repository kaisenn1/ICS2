import random
import pygame

white = (255, 255, 255)
black = (0, 0, 0)

system_font = pygame.font.get_default_font()
screen = pygame.display.set_mode((640, 480))
star = pygame.image.load('star.png')
rectangle = pygame.image.load('rectangle.png')
triangle = pygame.image.load('triangle.png')
shapes = [rectangle, star, triangle]
collisions = []


class MatchingShape:

    def __init__(self):
        self.rect = None
        self.score = 0

    def rand_shape(self, shape, callback):
        self.rect = shape.get_rect()
        self.rect.center = (random.randint(0, 640), random.randint(0, 480))
        screen.blit(shape, self.rect)
        pygame.display.update()
        callback(self.rect)

    def collision_test(self, shape_rect):
        collided = False
        while not collided:
            for event in pygame.event.get():
                if shape_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.score += 1
                    screen.fill(white)
                    scoreboard()
                    pygame.display.update()
                    collided = True
                if not shape_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    font = pygame.font.SysFont(system_font, 50)
                    text = font.render('Fail! You Clicked the Wrong Area!', True, black)
                    high_score = font.render('High Score: ' + str(self.score), True, black)
                    center = text.get_rect(center=(320, 220))
                    below_center = high_score.get_rect(center=(320, 260))
                    screen.fill(white)
                    screen.blit(text, center)
                    screen.blit(high_score, below_center)
                    pygame.display.update()



matching_shape = MatchingShape()


def randoms():
    image = random.choice(shapes)
    return image


def trick_shape(shape):
    collisions.clear()
    images = shapes
    images.remove(shape)
    for i in range(6):
        for item in images:
            rect = item.get_rect()
            rect.center = (random.randint(0, 640), random.randint(50, 480))
            if rect.collidelist(collisions) <= -1:
                screen.blit(item, rect)
                collisions.append(rect)
    pygame.display.update()
    images.append(shape)


def scoreboard():
    font = pygame.font.SysFont(system_font, 50)
    text = font.render('Score: ' + str(matching_shape.score), True, black)
    center = text.get_rect(center=(80, 20))
    screen.blit(text, center)


previous_time = pygame.time.get_ticks()
cooldown = 1000

pygame.init()
pygame.font.init()
screen.fill(white)

Running = True
while Running:

    random_shape = randoms()
    trick_shape(random_shape)
    matching_shape.rand_shape(random_shape, matching_shape.collision_test)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
