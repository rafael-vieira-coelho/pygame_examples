#!/usr/bin/env python
import random

from game_functions import desenha_retangulo


class Apple(object):

    def __init__(self, settings):
        self.s = settings
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.escolhe_posicao_aleatoria()

    def escolhe_posicao_aleatoria(self):
        self.position = (random.randint(0, self.s.GRID_WIDTH - 1) * self.s.GRIDSIZE, random.randint(0, self.s.GRID_HEIGHT - 1) * self.s.GRIDSIZE)

    def desenha(self):
        desenha_retangulo(self.color, self.position, self.s)
