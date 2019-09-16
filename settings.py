import pygame

class Settings():

    def __init__(self):
        self.FPS = 5
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 640, 480
        self.GRIDSIZE = 10
        self.GRID_WIDTH = self.SCREEN_WIDTH / self.GRIDSIZE
        self.GRID_HEIGHT = self.SCREEN_HEIGHT / self.GRIDSIZE
        self.UP = (0, -1)
        self.DOWN = (0, 1)
        self.LEFT = (-1, 0)
        self.RIGHT = (1, 0)
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.screen.blit(self.surface, (0, 0))

