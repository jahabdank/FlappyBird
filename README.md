# Flappy Bird Clone

This is a Flappy Bird clone implemented in Python using the Pygame library.

It was fully created using GenAI. I started by doing the first draft in OpenAI’s o1 model. Then I created a project in Cursor and continued from there. Not a single character of code was written by me; all was done using English language descriptions for changes to the game or code (refactoring, new features) as well as bugs (I only described the issues, and Cursor self-identified the fixes).

GenAI is already amazing, but it is still not perfect. However, the biggest issue I faced was technical—namely, that the output context window of a model was too short, so I had to force it to implement changes in parts. Additionally, I am a decent programmer myself, which helped me guide the process and correct the code when issues were found.

The models need to improve in human-in-the-loop ways of working. They try to do too much at once and need to be guided by the user more. However, they are amazing tools and will only get better over time.

## Description

This game is a recreation of the popular Flappy Bird game, with additional features and improvements. The player controls a bird, attempting to fly between columns of green pipes without hitting them. The game features:

- Simple one-button gameplay
- Randomly generated pipes
- Score tracking
- Game over screen with restart option
- High score tracking with persistent storage
- Hall of Fame showing top 10 scores with timestamps
- Configurable game parameters via JSON file
- Optimized logging system for debugging and analysis
- Modular code structure for easy maintenance and extension

## Project Structure

```
flappy_bird/
│
├── config.json
├── main.py
├── game_state.py
├── game_state_machine.py
├── entities/
│   ├── __init__.py
│   ├── bird.py
│   └── pipe.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   └── high_score_manager.py
└── README.md
```

## Getting Started

### Dependencies

To run this game, you'll need:

- Python 3.x
- Pygame library

### Installing

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install Pygame by running the following command in your terminal:

   ```bash
   pip install pygame
   ```

3. Clone this repository or download the source code.

### Executing the Game

1. Navigate to the project directory in your terminal.
2. Run the following command:

   ```bash
   python main.py
   ```

## How to Play

- Press the SPACE bar to make the bird flap and fly upwards.
- Navigate the bird through the gaps between the pipes.
- Each successfully passed pipe pair earns you one point.
- The game ends if the bird collides with a pipe or the ground.

## Configuration

Game parameters can be adjusted in the `config.json` file. This includes screen dimensions, game physics, visual settings, and more. You can also set the `LOG_LEVEL` to control the verbosity of the logging.

## Logging

The game includes an optimized logging system. Logs are stored in the `logs` directory, with a new log file created for each game session. Logs include information about game events, score changes, and any errors that might occur during gameplay.

## High Scores

High scores are persistently stored in a CSV file. The game keeps track of the top 10 scores, which are displayed in the Hall of Fame screen. The high score system has been optimized to efficiently load and display scores.

## Authors

Josef Habdank

## Version History

* 1.3
    * Removed unused configuration parameters
    * Ensured consistent use of configuration parameters throughout the code
* 1.2
    * Optimized high score loading and logging
    * Fixed issue with Hall of Fame not showing all historical scores
    * Added LOG_LEVEL configuration option
* 1.1
    * Refactored code to separate GameState and GameStateMachine
    * Improved project structure with modular design
    * Enhanced configuration system
    * Improved logging functionality
* 1.0
    * Refactored the game code to use a GameState class
* 0.9
    * Added comprehensive logging system
* 0.8
    * Updated Hall of Fame to highlight the current score in red if it made it to the top 10
* 0.7
    * Updated Hall of Fame to show top 10 scores from all recorded games
* 0.6
    * Added MD5 hash of config file to score records
* 0.5
    * Moved hardcoded constants to config.json file
* 0.4
    * Added persistent score tracking in a CSV file
    * Included game version in score records
* 0.3
    * Added timestamps to Hall of Fame entries
    * Fixed high score tracking bug
* 0.2
    * Added High Score tracking
    * Implemented Hall of Fame screen showing top 10 scores
    * Updated game over sequence to include high score and Hall of Fame screens
* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Original Flappy Bird game](https://en.wikipedia.org/wiki/Flappy_Bird)
* [Pygame documentation](https://www.pygame.org/docs/)
