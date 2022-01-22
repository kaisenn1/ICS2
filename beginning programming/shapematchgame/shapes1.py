import random
import pygame

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((640, 480))
star = pygame.image.load('star.png')
rectangle = pygame.image.load('rectangle.png')
triangle = pygame.image.load('triangle.png')
shapes = [rectangle, star, triangle]


class MatchingShape:

    def __init__(self):
        self.x = None
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


matching_shape = MatchingShape()


def randoms():
    image = random.choice(shapes)
    return image


def trick_shape(shape):
    images = shapes
    images.remove(shape)
    for item in images:
        for i in range(3):
            rect = item.get_rect()
            rect.center = (random.randint(50, 490), random.randint(50, 430))
            screen.blit(item, rect)
    images.append(shape)


def scoreboard():
    system_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(system_font, 50)
    text = font.render('Score: ' + str(matching_shape.score), 1, black)
    center = text.get_rect(center=(80, 20))
    screen.blit(text, center)


previous_time = pygame.time.get_ticks()
cooldown = 1000

pygame.init()
screen.fill(white)
Running = True
while Running:

    current_time = pygame.time.get_ticks()
    if current_time - previous_time >= cooldown:
        previous_time = pygame.time.get_ticks()
        random_shape = randoms()
        print(random_shape)
        trick_shape(random_shape)
        matching_shape.rand_shape(random_shape, matching_shape.collision_test)

        print(random_shape)
pygame.quit()
