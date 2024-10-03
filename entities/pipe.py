import pygame
import random
from utils.config import CONFIG

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = CONFIG['PIPE_WIDTH']
        self.gap_y = random.randint(100, CONFIG['SCREEN_HEIGHT'] - CONFIG['PIPE_GAP'] - 100)
        self.gap_height = CONFIG['PIPE_GAP']
        self.color = (0, 255, 0)  # Green color for pipes
        self.passed = False

    def update(self):
        self.x -= CONFIG['PIPE_SPEED']

    def draw(self, surface):
        # Draw top pipe
        top_height = self.gap_y
        pygame.draw.rect(surface, self.color, (self.x, 0, self.width, top_height))

        # Draw bottom pipe
        bottom_y = self.gap_y + self.gap_height
        bottom_height = CONFIG['SCREEN_HEIGHT'] - bottom_y
        pygame.draw.rect(surface, self.color, (self.x, bottom_y, self.width, bottom_height))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.gap_y)

    def get_bottom_rect(self):
        bottom_y = self.gap_y + self.gap_height
        bottom_height = CONFIG['SCREEN_HEIGHT'] - bottom_y
        return pygame.Rect(self.x, bottom_y, self.width, bottom_height)

    def is_off_screen(self):
        return self.x + self.width < 0
