from random import random

from pygame import Vector2
from pygame.math import Vector3


class Creep:
    def __init__(self):
        self.taille = 3
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0, largeur), random.randint(-largeur,0))

    def mourir(self):
        pass

    def afficher(self):
        pass

