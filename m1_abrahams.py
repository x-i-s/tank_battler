import pygame
import math

class M1Abrams:
    """A class to manage tanks"""

    def __init__(self, ai_game):
        """Initialize the tank and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the tank image and get its rect.
        self.image = pygame.image.load('images/player_character/m1_abrams.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        #start each new tank at the centre of the screen
        self.rect.center = self.screen_rect.center
        self.angle = 0
        self.rotation_speed = 1.5
        self.m1_abrams_speed = 2
                
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.rotate_clockwise = False
        self.rotate_counter_clockwise = False
        self.moving_forward = False
        self.moving_backwards = False
    
    def update(self):
        """Update the tank's position based on movement flags."""
        if self.rotate_clockwise:
            self.angle -= self.rotation_speed
        if self.rotate_counter_clockwise:
            self.angle += self.rotation_speed
        if self.moving_forward:
            self.move_forward()
        if self.moving_backwards:
            self.move_backward()
       
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_image.get_rect(center=self.rect.center)
        self.rect.y = self.y
        self.rect.x = self.x
        

    def move_forward(self):
        """Move the tank forward along its facing axis."""
        angle_rad = math.radians(self.angle)
        dx = -self.m1_abrams_speed * math.cos(angle_rad)
        dy = self.m1_abrams_speed * math.sin(angle_rad)
        new_x = self.x + dx
        new_y = self.y + dy
        if (0 <= new_x <= self.screen_rect.width - self.rect.width) and \
        (0 <= new_y <= self.screen_rect.height - self.rect.height):
            self.x = new_x
            self.y = new_y

    def move_backward(self):
        """Move the tank backward along its facing axis."""
        angle_rad = math.radians(self.angle)
        dx = self.m1_abrams_speed * math.cos(angle_rad)
        dy = -self.m1_abrams_speed * math.sin(angle_rad)
        new_x = self.x + dx
        new_y = self.y + dy
        if (0 <= new_x <= self.screen_rect.width - self.rect.width) and \
        (0 <= new_y <= self.screen_rect.height - self.rect.height):
            self.x = new_x
            self.y = new_y


        


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.rotated_image, self.rotated_rect)