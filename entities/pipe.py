import pygame
import random
from utils.config import CONFIG

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = CONFIG['PIPE_WIDTH']
        self.gap_y = random.randint(100, CONFIG['SCREEN_HEIGHT'] - CONFIG['PIPE_GAP'] - 100)
        self.gap_height = CONFIG['PIPE_GAP']
        self.color = CONFIG['PIPE_COLOR']
        self.passed = False

    def update(self):
        self.x -= CONFIG['PIPE_SPEED']

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, 0, self.width, self.gap_y))
        pygame.draw.rect(surface, self.color, (self.x, self.gap_y + self.gap_height, 
                         self.width, CONFIG['SCREEN_HEIGHT'] - (self.gap_y + self.gap_height)))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.gap_y)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.gap_y + self.gap_height, self.width, 
                           CONFIG['SCREEN_HEIGHT'] - (self.gap_y + self.gap_height))

    def is_off_screen(self):
        return self.x + self.width < 0
