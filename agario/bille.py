import random

from pygame.math import Vector2


class Bille:
    def __init__(self):

        self.taille = 3
        self.position = Vector2(random.randint(0, 400), random.randint(-400, 0))
        self.direction = Vector2(random.randint(0, 400), random.randint(-400, 0))

    def suivre(self):
        pass

    def mourir(self):
        pass

    def manger(self):
        pass

    def afficher(self):
        pass
