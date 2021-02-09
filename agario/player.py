from random import random

from pygame.math import Vector2, Vector3


class Player:
    def __init__(self):
        self.taille = 3
        self.vitesse = 5
        self.forme = "circle"
        self.position = Vector2(random.randint(0, largeur), random.randint(-largeur, 0))
        self.direction = Vector2(random.randint(0, largeur), random.randint(-largeur, 0))
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self):
        pass

    def afficher(self):
        pass
