import pygame
from datetime import datetime
from game_state import GameState
from entities.pipe import Pipe
from utils.logger import logger
from utils.config import CONFIG
from utils.high_score_manager import save_score_to_csv, load_high_scores

class GameStateMachine:
    def __init__(self):
        self.state = GameState()
        self.load_high_scores()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def reset(self):
        self.state = GameState()
        self.load_high_scores()
        logger.info("Game reset")

    def update(self):
        if not self.state.game_over:
            self.state.bird.update()
            
            for pipe in self.state.pipes:
                pipe.update()
            
            self.state.pipes = [pipe for pipe in self.state.pipes if pipe.x + CONFIG['PIPE_WIDTH'] > 0]
            
            while len(self.state.pipes) < 3:
                new_x = max(pipe.x for pipe in self.state.pipes) + CONFIG['PIPE_SPACING']
                self.state.pipes.append(Pipe(new_x))
            
            for pipe in self.state.pipes:
                if not pipe.passed and pipe.x + CONFIG['PIPE_WIDTH'] < self.state.bird.x:
                    pipe.passed = True
                    self.state.score += 1
                    logger.info(f"Score increased to {self.state.score}")

            self.check_collisions()

    def check_collisions(self):
        bird_rect = self.state.bird.get_rect()
        for pipe in self.state.pipes:
            if bird_rect.colliderect(pipe.get_top_rect()) or bird_rect.colliderect(pipe.get_bottom_rect()):
                self.game_over()
                return

        if self.state.bird.y + self.state.bird.height >= CONFIG['SCREEN_HEIGHT'] - CONFIG['GROUND_HEIGHT']:
            self.game_over()

    def game_over(self):
        self.state.game_over = True
        self.state.current_game_datetime = datetime.now().replace(microsecond=0)
        logger.info(f"Game over. Final score: {self.state.score}")
        self.save_high_score()

    def flap(self):
        if not self.state.game_over:
            self.state.bird.flap()
            logger.debug("Bird flapped")

    def save_high_score(self):
        save_score_to_csv(self.state.score, self.state.current_game_datetime)
        self.load_high_scores()

    def load_high_scores(self):
        self.state.high_scores = load_high_scores()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.state.game_over:
                if self.state.show_hall_of_fame:
                    self.reset()
                elif self.state.show_high_score:
                    self.state.show_hall_of_fame = True
                    logger.info("Showing Hall of Fame")
                else:
                    self.state.show_high_score = True
                    logger.info("Showing High Score")
            else:
                self.flap()

    def draw(self, screen):
        screen.fill(CONFIG['BACKGROUND_COLOR'])

        if self.state.game_over:
            if self.state.show_hall_of_fame:
                self.draw_hall_of_fame(screen)
            elif self.state.show_high_score:
                self.draw_high_score(screen)
            else:
                self.draw_game_over(screen)
        else:
            self.state.bird.draw(screen)
            for pipe in self.state.pipes:
                pipe.draw(screen)
            pygame.draw.rect(screen, CONFIG['GROUND_COLOR'], (0, CONFIG['SCREEN_HEIGHT'] - CONFIG['GROUND_HEIGHT'], CONFIG['SCREEN_WIDTH'], CONFIG['GROUND_HEIGHT']))

            score_surface = self.font.render(str(self.state.score), True, CONFIG['TEXT_COLOR'])
            screen.blit(score_surface, (CONFIG['SCREEN_WIDTH'] / 2 - score_surface.get_width() / 2, 20))

    def draw_hall_of_fame(self, screen):
        title_surface = self.font.render('Hall of Fame', True, CONFIG['GAME_OVER_COLOR'])
        screen.blit(title_surface, (CONFIG['SCREEN_WIDTH'] / 2 - title_surface.get_width() / 2, 50))
        
        for i, (high_score, date_time) in enumerate(self.state.high_scores):
            score_text = f'{i+1}. {high_score} - {date_time.strftime("%Y-%m-%d %H:%M:%S")}'
            color = CONFIG['GAME_OVER_COLOR'] if high_score == self.state.score and date_time == self.state.current_game_datetime else CONFIG['TEXT_COLOR']
            score_surface = self.small_font.render(score_text, True, color)
            screen.blit(score_surface, (CONFIG['SCREEN_WIDTH'] / 2 - score_surface.get_width() / 2, 120 + i * 40))
        
        restart_text = 'Press SPACE to restart'
        restart_surface = self.small_font.render(restart_text, True, CONFIG['TEXT_COLOR'])
        screen.blit(restart_surface, (CONFIG['SCREEN_WIDTH'] / 2 - restart_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] - 100))

    def draw_high_score(self, screen):
        game_over_surface = self.font.render('Game Over', True, CONFIG['GAME_OVER_COLOR'])
        screen.blit(game_over_surface, (CONFIG['SCREEN_WIDTH'] / 2 - game_over_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] / 3 - game_over_surface.get_height() / 2))
        
        score_text = f'Score: {self.state.score}'
        score_surface = self.font.render(score_text, True, CONFIG['TEXT_COLOR'])
        screen.blit(score_surface, (CONFIG['SCREEN_WIDTH'] / 2 - score_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] / 2 - score_surface.get_height() / 2))
        
        high_score_text = f'High Score: {self.state.high_scores[0][0] if self.state.high_scores else 0}'
        high_score_surface = self.font.render(high_score_text, True, CONFIG['TEXT_COLOR'])
        screen.blit(high_score_surface, (CONFIG['SCREEN_WIDTH'] / 2 - high_score_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] / 2 + high_score_surface.get_height()))
        
        continue_text = 'Press SPACE to see Hall of Fame'
        continue_surface = self.small_font.render(continue_text, True, CONFIG['TEXT_COLOR'])
        screen.blit(continue_surface, (CONFIG['SCREEN_WIDTH'] / 2 - continue_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] * 3 / 4))

    def draw_game_over(self, screen):
        game_over_surface = self.font.render('Game Over', True, CONFIG['GAME_OVER_COLOR'])
        screen.blit(game_over_surface, (CONFIG['SCREEN_WIDTH'] / 2 - game_over_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] / 2 - game_over_surface.get_height() / 2))
        
        continue_text = 'Press SPACE to continue'
        continue_surface = self.small_font.render(continue_text, True, CONFIG['TEXT_COLOR'])
        screen.blit(continue_surface, (CONFIG['SCREEN_WIDTH'] / 2 - continue_surface.get_width() / 2, CONFIG['SCREEN_HEIGHT'] * 3 / 4))