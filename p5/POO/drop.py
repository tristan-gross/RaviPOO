import random

import pygame
from pygame import Vector2

import core


class Drop:
    def __init__(self):
        self.gravity = random.randint(5,10)
        self.size = random.randint(5,10)
        self.r = random.randint(0,255)
        self.v = random.randint(0,255)
        self.b = random.randint(0,255)
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400,0))

    def tomber(self,taille):
        self.position[1] = self.position[1] + self.gravity
        if self.position[1] > taille:
            self.raz()

    def raz(self):
        self.position[1] = 0
    def afficher(self,core):
        pygame.draw.line(core.screen, (self.r,self.v,self.b ), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)