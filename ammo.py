import pygame
from pygame.sprite import Sprite
import math

class Ammo(Sprite):
    """A class to manage ammo fired from tank"""

    def __init__(self, ai_game):
        """Create a shell object at the tanks current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.shell_colour
        self.angle = ai_game.m1_abrams.angle
        

        #create a shell rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, self.settings.shell_width,
            self.settings.shell_height)
        self.rect.center = ai_game.m1_abrams.rect.center

        #store shells position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the shell across the screen."""
        #update the exact position of the bullet
        angle_rad = math.radians(self.angle)
        dx = -self.settings.shell_speed * math.cos(angle_rad)
        dy = self.settings.shell_speed * math.sin(angle_rad)
        self.rect.x += dx
        self.rect.y += dy
        

    def draw_shell(self):
        """Draw the shell to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)