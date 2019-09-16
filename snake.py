#!/usr/bin/env python
import random, pygame

from game_functions import desenha_retangulo


class Snake():

    def __init__(self, settings):
        self.s = settings
        self.lose()
        self.color = (0, 0, 0)

    def get_head_position(self):
        return self.positions[0]

    def lose(self):
        self.length = 1
        self.positions = [((self.s.SCREEN_WIDTH / 2), (self.s.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([self.s.UP, self.s.DOWN, self.s.LEFT, self.s.RIGHT])

    def point(self, pt):
        if self.length > 1 and (pt[0] * -1, pt[1] * -1) == self.direction:
            return
        else:
            self.direction = pt

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * self.s.GRIDSIZE)) % self.s.SCREEN_WIDTH), (cur[1] + (y * self.s.GRIDSIZE)) % self.s.SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.lose()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def desenha(self):
        for p in self.positions:
            desenha_retangulo(self.color, p, self.s)

