import random
shapes = ['star','triangle','rectangle']

class MatchingShape:

    def rand_shape(self):
        image = random.choice(shapes)
        print(image)
        self.gone = image


    def trick_shape(self):
        shapes = ['star','triangle','rectangle']
        shapes.remove(self.gone)
        print(shapes)

x = MatchingShape()
x.rand_shape()
x.trick_shape()