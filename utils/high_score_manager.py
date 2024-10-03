import csv
import os
from datetime import datetime
from utils.config import CONFIG, CONFIG_HASH
from utils.logger import logger

def save_score_to_csv(score, current_game_datetime):
    """
    Save the current game score to the CSV file.
    """
    file_exists = os.path.isfile(CONFIG['SCORES_FILE'])
    
    try:
        with open(CONFIG['SCORES_FILE'], 'a', newline='') as csvfile:
            fieldnames = ['score', 'datetime', 'version', 'config_hash']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow({
                'score': score, 
                'datetime': current_game_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'version': CONFIG['GAME_VERSION'],
                'config_hash': CONFIG_HASH
            })
        logger.info(f"Saved score {score} at {current_game_datetime}")
    except IOError as e:
        logger.error(f"Error saving score to CSV: {e}")

def load_high_scores():
    """
    Load high scores from the CSV file.
    """
    high_scores = []
    if os.path.exists(CONFIG['SCORES_FILE']):
        try:
            with open(CONFIG['SCORES_FILE'], 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    high_scores.append((
                        int(row['score']), 
                        datetime.strptime(row['datetime'], "%Y-%m-%d %H:%M:%S")
                    ))
        except IOError as e:
            logger.error(f"Error loading high scores from CSV: {e}")
        except ValueError as e:
            logger.error(f"Error parsing high scores from CSV: {e}")
    
    # Sort high scores in descending order and keep only the top scores
    high_scores.sort(key=lambda x: x[0], reverse=True)
    high_scores = high_scores[:CONFIG['MAX_HIGH_SCORES']]
    
    logger.info(f"Loaded {len(high_scores)} high scores")
    return high_scores

def clear_high_scores():
    """
    Clear all high scores by deleting the scores file.
    """
    if os.path.exists(CONFIG['SCORES_FILE']):
        try:
            os.remove(CONFIG['SCORES_FILE'])
            logger.info("High scores cleared")
        except OSError as e:
            logger.error(f"Error clearing high scores: {e}")
    else:
        logger.info("No high scores file to clear")

def get_highest_score():
    """
    Get the highest score from the CSV file.
    """
    high_scores = load_high_scores()
    if high_scores:
        return high_scores[0][0]
    return 0
