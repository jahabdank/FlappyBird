import pygame
import sys
from game_state_machine import GameStateMachine
from utils.logger import logger
from utils.config import CONFIG

# Initialize Pygame
pygame.init()
logger.info("Pygame initialized")

# Screen setup
SCREEN = pygame.display.set_mode((CONFIG['SCREEN_WIDTH'], CONFIG['SCREEN_HEIGHT']))
pygame.display.set_caption('Flappy Bird')

def main():
    clock = pygame.time.Clock()
    game_state_machine = GameStateMachine()
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                logger.info("Game quit by user")
                return
            game_state_machine.handle_event(event)

        game_state_machine.update()
        game_state_machine.draw(SCREEN)
        pygame.display.update()

    pygame.quit()
    logger.info("Game ended")
    sys.exit()

if __name__ == '__main__':
    main()
