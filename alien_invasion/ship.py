import pygame

# class to handle ship objects
class Ship:
    # Initialize a ship and pass it the game instance
    def __init__(self, ai_game):
        # Ships screen = the game screen
        self.screen = ai_game.screen
        # Set the ship's settings to the game's settings
        self.settings = ai_game.settings
        # The ships screen rectangle = the game screen rectangle
        self.screen_rect = ai_game.screen.get_rect()
        # Upload an image to use
        self.image = pygame.image.load('images/ship.bmp')
        # Ships rectangle = the image's rectangle
        self.rect = self.image.get_rect()
        # Set the ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value fo the ships (Horizontal) pos
        self.x = float(self.rect.x)
        # Movement flag (R)
        self.moving_right = False
        # Movement flag (L)
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x

    # Basically the draw method for the image
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)