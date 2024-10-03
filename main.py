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

# Font setup
FONT = pygame.font.Font(None, 36)

def main():
    clock = pygame.time.Clock()
    game_state_machine = GameStateMachine()
    running = True

    while running:
        clock.tick(CONFIG['FPS'])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                logger.info("Game quit by user")
                return
            game_state_machine.handle_event(event)

        game_state_machine.update()
        
        # Clear the screen
        SCREEN.fill(CONFIG['BACKGROUND_COLOR'])
        
        # Draw the game state
        game_state_machine.draw(SCREEN)
        
        # Draw FPS
        fps = str(int(clock.get_fps()))
        fps_text = FONT.render(f"FPS: {fps}", 1, CONFIG['TEXT_COLOR'])
        SCREEN.blit(fps_text, (10, 10))
        
        pygame.display.update()

    pygame.quit()
    logger.info("Game ended")
    sys.exit()

if __name__ == '__main__':
    main()
