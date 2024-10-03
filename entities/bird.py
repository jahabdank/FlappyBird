import pygame
from utils.config import CONFIG

class Bird:
    def __init__(self):
        self.x = CONFIG['BIRD_X']
        self.y = CONFIG['SCREEN_HEIGHT'] / 2
        self.vel_y = 0
        self.width = 30
        self.height = 30
        self.image = self.create_bird_image()

    def create_bird_image(self):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.circle(surface, (255, 255, 0), (self.width // 2, self.height // 2), self.width // 2)
        return surface

    def update(self):
        self.vel_y += CONFIG['GRAVITY']
        self.y += self.vel_y

        # Prevent the bird from going off the top of the screen
        if self.y < 0:
            self.y = 0
            self.vel_y = 0

    def flap(self):
        self.vel_y = CONFIG['FLAP_STRENGTH']

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
