import pygame
rectangle = pygame.Rect(5, 5, 20, 20) # x, y, width, height

def is_over(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False

pos = pygame.mouse.get_pos() # gets the current mouse coords
if is_over(rectangle, pos): # pass in the pygame.Rect and the mouse coords
    print('The mouse is over the rectangle')
else:
    print('The mouse is not over the rectangle')