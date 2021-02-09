from random import random

from pygame.math import Vector2


class Bille:
    def __init__(self):
        self.vitesse = 5
        self.taille =3
        self.position = Vector2(random.randint(0, largeur), random.randint(-largeur, 0))
        self.direction = Vector2(random.randint(0, largeur), random.randint(-largeur, 0))

    def suivre(self):
        pass
    def mourir(self):
        pass
    def manger(self):
        pass
    def afficher(self):
        pass
