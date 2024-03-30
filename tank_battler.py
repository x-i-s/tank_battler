import sys
import pygame
from settings import Settings
from m1_abrahams import M1Abrams
from ammo import Ammo


class TankBattler:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Tank Battler')
        self.m1_abrams = M1Abrams(self)
        self.shells = pygame.sprite.Group()

        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()   
            self.m1_abrams.update() 
            self.shells.update()
            self._remove_offscreen_shells()
            self._update_screen()            
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)                  
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):
        """respond to key presses"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.m1_abrams.rotate_clockwise = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.m1_abrams.rotate_counter_clockwise = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.m1_abrams.moving_forward = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.m1_abrams.moving_backwards = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_shell()

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.m1_abrams.rotate_clockwise = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.m1_abrams.rotate_counter_clockwise = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.m1_abrams.moving_forward = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.m1_abrams.moving_backwards = False 

    def _fire_shell(self):
        """Create a new shell and add it to the shells group."""
        new_shell = Ammo(self)
        self.shells.add(new_shell)
                

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        for shell in self.shells.sprites():
            shell.draw_shell()
        self.m1_abrams.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

    def _remove_offscreen_shells(self):
        """Remove shells that have gone off-screen"""
        screen_rect = pygame.Rect((0, 0), (self.settings.screen_width, self.settings.screen_height))
        for shell in self.shells.copy():
            if not screen_rect.colliderect(shell.rect):
                self.shells.remove(shell)


if __name__ == "__main__":
    """Make a game instance and run the game"""
    tb = TankBattler()
    tb.run_game()