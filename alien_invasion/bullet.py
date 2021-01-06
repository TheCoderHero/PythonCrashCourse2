import pygame
from pygame.sprite import Sprite

# class for managing the bullet
class Bullet(Sprite):

    def __init__(self, ai_game):
        # Initialize Sprite object (super class = Sprite)
        super().__init__()
        # Setup settings for the bullet
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create (from Rect() method) a bullet at pos (0, 0) then adjust
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's pos as a decimal
        self.y = float(self.rect.y)
    
    def update(self):
        # Manage bullet pos
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)