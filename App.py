import pygame
import sys
from Settings import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.startScreen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run(self):
        pygame.display.set_caption("Petar's App")
        while self.running:
            if self.state == 'start':
                self.state_event()
                self.state_draw()
            self.clock.tick(120)
        pygame.quit()
        sys.exit()

    def state_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def state_draw(self):
        self.startScreen.fill(WHITE)
        pygame.display.update()