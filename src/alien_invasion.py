import sys
import pygame

class AlienInvasion:
    """
    @desc : main class to manage game assets and behaviour
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))

        # set caption of the game
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        @desc: Start the main loop
        """
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recent drawn screen visible
            pygame.display.flip()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()