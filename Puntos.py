import pygame
from pygame.locals import *


class Puntos(pygame.sprite.Sprite):

    def __init__(self, valor, x, y, pantalla):
        super(Puntos, self).__init__()
        self.valor = valor
        self.presionada = False
        self.x = x
        self.y = y
        self.pantalla = pantalla
        self.circulo = pygame.draw.circle(self.pantalla, (0, 0, 0),
        (self.x, self.y), 15)

    def presionar(self):
        self.presionada = not self.presionada

    def pintarPunto(self):
        if(self.presionada is True):
            self.circulo = pygame.draw.circle(self.pantalla, (255, 0, 0),
            (self.x, self.y), 15)
        else:
            self.circulo = pygame.draw.circle(self.pantalla, (0, 0, 0),
            (self.x, self.y), 15)