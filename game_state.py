from entities.bird import Bird
from entities.pipe import Pipe
from utils.config import CONFIG

class GameState:
    def __init__(self):
        self.bird = Bird()
        self.pipes = [Pipe(CONFIG['SCREEN_WIDTH'] + i * CONFIG['PIPE_SPACING']) for i in range(3)]
        self.score = 0
        self.game_over = False
        self.show_high_score = False
        self.show_hall_of_fame = False
        self.current_game_datetime = None
        self.high_scores = []
