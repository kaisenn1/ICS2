# Title: Shape Match Game
# Author: Kaisen
# Date: January 21, 2022
import random
import pygame

white = (255, 255, 255)
black = (0, 0, 0)

system_font = pygame.font.get_default_font()
screen = pygame.display.set_mode((640, 480))
star = pygame.image.load('star.png')
plain_square = pygame.image.load('square.png')
triangle = pygame.image.load('triangle.png')
square = pygame.transform.scale(plain_square, (80, 80))
shapes = [square, star, triangle]
collisions = []


class MatchingShape:  # easier interaction between functions

    def __init__(self):
        self.rect = None
        self.score = 0

    def rand_shape(self, shape, callback):
        self.rect = shape.get_rect()
        self.rect.center = (random.randint(0, 640), random.randint(75, 480))
        screen.blit(shape, self.rect)
        pygame.display.update()
        callback(self.rect)

    def collision_test(self, shape_rect):
        not_collided = True
        while not_collided:  # not collided looks better
            for event in pygame.event.get():  # tests mouse collision
                if shape_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:  # if mouse clicks the correct shape, add score and reset
                    self.score += 1
                    screen.fill(white)
                    pygame.display.update()
                    not_collided = False
                if not shape_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:  # if mouse does not click the correct shape or space around the shape, run end game func
                    end_scoreboard()


matching_shape = MatchingShape()


def randoms():  # random shape func
    image = random.choice(shapes)
    return image


def trick_shape(shape):  # shapes meant to distract from the single main shape
    collisions.clear()
    images = shapes
    images.remove(shape)
    for i in range(6):
        for item in images:
            rect = item.get_rect()
            rect.center = (random.randint(0, 640), random.randint(75, 480))
            if rect.collidelist(collisions) <= -1:  # checks if trick shape will overlap with another trick shape
                screen.blit(item, rect)
                collisions.append(rect)  # adds shape to list of taken positions
    pygame.display.update()
    images.append(shape)  # needs to be put back after being temporarily removed or list will get smaller and smaller


def scoreboard(rand_shape):
    font = pygame.font.SysFont(system_font, 50)
    text = font.render('Score: ' + str(matching_shape.score), True, black)
    shape = font.render('Shape:', True, black)
    matched_shape = pygame.transform.scale(rand_shape, (25, 25))
    shape_center = text.get_rect(center=(550, 20))
    center = text.get_rect(center=(80, 20))
    matched_shape_center = matched_shape.get_rect(center=(620, 19))
    screen.blit(text, center)
    screen.blit(shape, shape_center)
    screen.blit(matched_shape, matched_shape_center)


def end_scoreboard():
    font = pygame.font.SysFont(system_font, 50)
    text = font.render('Fail! You Clicked the Wrong Area!', True, black)
    high_score = font.render('High Score: ' + str(matching_shape.score), True, black)
    center = text.get_rect(center=(320, 220))
    below_center = high_score.get_rect(center=(320, 260))
    screen.fill(white)
    screen.blit(text, center)
    screen.blit(high_score, below_center)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    exit('Fail')


pygame.init()
pygame.font.init()
screen.fill(white)
running = True
while running:
    random_shape = randoms()  # get a random shape
    pygame.time.delay(100)
    scoreboard(random_shape)
    trick_shape(random_shape)  # pass random shape into trick shape so trick shapes cannot be the chosen random shape
    matching_shape.rand_shape(random_shape, matching_shape.collision_test)  # pass random shape as main shape


pygame.quit()
