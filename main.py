#!/usr/bin/env python

import pygame
import time
import random

from pygame.locals import *
from snake import Snake
from apple import Apple
from settings import Settings
from game_functions import *

if __name__ == '__main__':
    s = Settings()
    pygame.init()
    pygame.key.set_repeat(1, 40)
    snake = Snake(s)
    apple = Apple(s)
    while True:
        for evento in pygame.event.get():
            testa_eventos(evento, snake, s)
        atualiza_tela(snake, apple, s)
