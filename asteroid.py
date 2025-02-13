from constants import *
from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)  # Add width=2 parameter

    def update(self, dt):
        self.position += self.velocity * dt