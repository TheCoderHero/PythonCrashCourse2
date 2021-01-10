# External Imports
# pygame module contains a library of functions used to create games
import pygame
# sys module used to close the game
import sys
# Import sleep from the Time Module
from time import sleep

# Internal Imports
# Import settings from the Settings Module
from settings import Settings
# Import ship from the Ship Module
from ship import Ship
# Import bullet from the Bullet Module
from bullet import Bullet
# Import alien from the Alien Module
from alien import Alien
# Import game_stats from GameStats Module
from game_stats import GameStats
# Import buttons from Buttons Module
from button import Button
# Import score from Scoreboard Module
from scoreboard import Scoreboard

# class to manage game assets and behavior
class AlienInvasion:
    # Initialization method
    def __init__(self):
        # Initialize the game and create game resources.
        pygame.init()
        # Initialize settings
        self.settings = Settings()
        # Create a pygame screen (surface) and set the screen dimensions
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Set the window title for the screen
        pygame.display.set_caption("Alien Invasion")
        # Initialize Game Stats
        self.stats = GameStats(self)
        # Initialize the scoreboard
        self.sb = Scoreboard(self)
        # Initialize a ship
        self.ship = Ship(self)
        # Initialize a Sprite Group to hold Bullets
        self.bullets = pygame.sprite.Group()
        # Initialize a Sprite Group to hold Aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Initialize the play button
        self.play_button = Button(self, "PLAY")

    # Game loop method
    def run_game(self):
        # Start the game loop
        while True:
            self._check_events()
            # If the player still has ships left...
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            # Update the screen as soon as the game loads
            self._update_screen()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_bullet_alien_collisions(self):
        # Check if any element from the bullets group and any element of the aliens group overlap, then delete them
        # pygame.sprite.groupcollide(GroupA, GroupB, DeleteA_bool, DeleteB_bool)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _check_events(self):
        # Event loop controlled by the run_game() function
        for event in pygame.event.get():
            # If the user clicks the close window button...
            if event.type == pygame.QUIT:
                # Close the window and shut down the game
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            if self.stats.score > self.stats.highest_score:
                with open('highscore.txt', 'w') as file_object:
                    file_object.write(str(self.stats.high_score))
            self.settings.initialize_dynamic_settings()

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        # Available space for columns
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Available space for rows
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _fire_bullet(self):
        # If player has not reached max allowed bullets...
        if len(self.bullets) < self.settings.bullets_allowed:
            # Create a new Bullet
            new_bullet = Bullet(self)
            # Add new Bullet to the Bullets Group
            self.bullets.add(new_bullet)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # pygame.sprite.spritecollideany(SpriteA, GroupB)
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_bullets(self):
        self.bullets.update()
        # Delete Bullets off screen
        for bullet in self.bullets.copy(): # Can not modify a list from FOR LOOP so we make a copy
            if bullet.rect.bottom <= 0: # if bullet has reached the top of the screen
                self.bullets.remove(bullet) # We modify the actual list (not the copy)
        # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Draw the ship on the screen
        self.ship.blitme()

        # Draw bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw alients on the screen
        self.aliens.draw(self.screen)

        # Draw the scoreboard in the upper right of the screen
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Draws the most recent view and hides the old view
        pygame.display.flip()

# If this file is ran directly...
if __name__=='__main__':
    # Create an instance of the game
    ai = AlienInvasion()
    # Start the game loop
    ai.run_game()