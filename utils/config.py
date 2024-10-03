import json
import os
import hashlib

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file at {config_path}")

def get_config_hash():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    try:
        with open(config_path, 'rb') as config_file:
            return hashlib.md5(config_file.read()).hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_path}")

# Load the configuration
CONFIG = load_config()

# Generate the configuration hash
CONFIG_HASH = get_config_hash()

# Validate required configuration keys
REQUIRED_KEYS = [
    'GAME_VERSION', 'SCREEN_WIDTH', 'SCREEN_HEIGHT', 'GRAVITY', 'FLAP_STRENGTH',
    'PIPE_GAP', 'PIPE_WIDTH', 'PIPE_SPEED', 'BIRD_X', 'PIPE_SPACING',
    'GROUND_HEIGHT', 'MAX_HIGH_SCORES', 'SCORES_FILE'
]

for key in REQUIRED_KEYS:
    if key not in CONFIG:
        raise KeyError(f"Missing required configuration key: {key}")

# You can add additional validation for specific values here if needed
# For example:
if CONFIG['SCREEN_WIDTH'] <= 0 or CONFIG['SCREEN_HEIGHT'] <= 0:
    raise ValueError("Screen dimensions must be positive")

if CONFIG['GRAVITY'] <= 0:
    raise ValueError("Gravity must be positive")

# Add more validations as needed...

print("Configuration loaded successfully.")
