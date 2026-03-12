from __future__ import annotations
import json
import os
from turtle import Turtle

# game grid settings
# the snake moves in steps of 20, so everything is based on this grid
GRID_WIDTH = 30
GRID_HEIGHT = 30
CELL_SIZE = 20

SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE


# scoreboard class
# keeps track of your current score and of the high score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.leaderboard_file = "snake_leaderboard.json"
        
        # load existing high scores
        self._load_high_scores()

        self.hideturtle()
        self.penup()
        self.color("white")

        # position the score at the top of the screen
        self.goto(0, SCREEN_HEIGHT / 2 - 40)
        self._draw()

    def _load_high_scores(self):
        """Load high scores from JSON file"""
        try:
            if os.path.exists(self.leaderboard_file):
                with open(self.leaderboard_file, 'r') as f:
                    data = json.load(f)
                    self.high_score = data.get('high_score', 0)
        except (json.JSONDecodeError, IOError):
            # If file is corrupted or unreadable, start fresh
            self.high_score = 0

    def _save_high_scores(self):
        """Save high scores to JSON file"""
        try:
            data = {'high_score': self.high_score}
            with open(self.leaderboard_file, 'w') as f:
                json.dump(data, f)
        except IOError:
            # If we can't save, continue without saving
            pass

    #draws or updates the score text
    def _draw(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center"
                   , font=("Arial", 16, "normal"))

    # increase score when food is eaten
    def increase_score(self, points: int):
        self.score += points

        # update high score if needed
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_scores()  # Save new high score

        self._draw()

    # reset score when the snake crashes and dies
    def reset(self):
        self.score = 0
        self._draw()


# Main execution (for testing only)
if __name__ == "__main__":
    print("screen.py only contains the Scoreboard class.")
    print("Please run 'python rungame.py' to start the game.")
