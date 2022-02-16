import pygame
import sys
from Settings import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 600))
        self.clock = pygame.time.Clock()
        self.title = pygame.
        self.running = True
        self.state = 'start'


    def run(self):
        pygame.display.set_caption("Petar's App")
        self.screen.fill(WHITE)
        while self.running:
            if self.state == 'start':
                self.state_event()
                self.state_update()
                self.state_draw()
            self.clock.tick(120)
        pygame.quit()
        sys.exit()

    def state_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def state_update(self):
        pass

    def state_draw(self):
        self.screen.fill(WHITE)
        pygame.display.update()
