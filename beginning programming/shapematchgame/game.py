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
        self.l = None
        self.image = None
        self.rect = None
        self.score = 0

    def rand_shape(self, callback):
        image = random.choice(shapes)
        images = [rectangle, star, triangle]
        images.remove(image)
        for item in images:
            print(images.index(item))
        self.l = images
        self.rect = image.get_rect()
        self.rect.center = (100, 100)
        screen.blit(image, self.rect)
        pygame.display.update()
        callback(self.rect)

    def trick_shape(self):
        for i in range(5):
            for item in self.l:
                print(self.l.index(item))
            shape = random.choice(self.l)
            rect = shape.get_rect()
            rect.center = (random.randint(0, 640), random.randint(0, 480))
            screen.blit(shape, rect)
            pygame.display.update()

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
        matching_shape.rand_shape(matching_shape.collision_test)
        matching_shape.trick_shape()
pygame.quit()
