import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os

def setup_logger():
    # Create logs directory if it doesn't exist
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create a unique log filename with timestamp
    log_filename = os.path.join(logs_dir, f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}_flappy_bird.log")

    # Create a logger
    logger = logging.getLogger('flappy_bird')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    file_handler = RotatingFileHandler(
        log_filename,
        maxBytes=1024 * 1024,  # 1 MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Create and configure the logger
logger = setup_logger()
