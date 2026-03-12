from __future__ import annotations
import json
import os
import time
from turtle import Screen, Turtle

from snake import Snake
from food import Food


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


# main game controller
# to connect everything together
class Game:
    def __init__(self):
        self.screen = Screen()
        self._setup_screen()

        # create game objects
        self.snake = Snake()
        self.food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.scoreboard = Scoreboard()

        self._setup_controls()

        # controls how fast the snake moves
        self.game_speed = 0.1
        self.game_is_on = True
        self.game_over = False
        
        # game over screen objects
        self.game_over_text = None
        self.restart_text = None

    # sets up the screen appearance
    def _setup_screen(self) -> None:
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Advanced Snake Game")
        self.screen.tracer(0)

    # connects arrow keys to snake movement
    def _setup_controls(self) -> None:
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self._restart_game, "space")  # Spacebar to restart

    def _show_game_over_screen(self):
        """Display game over screen with leaderboard"""
        # Create game over text
        self.game_over_text = Turtle()
        self.game_over_text.hideturtle()
        self.game_over_text.penup()
        self.game_over_text.color("red")
        self.game_over_text.goto(0, 50)
        self.game_over_text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        
        # Show final score
        final_score_text = Turtle()
        final_score_text.hideturtle()
        final_score_text.penup()
        final_score_text.color("white")
        final_score_text.goto(0, 0)
        final_score_text.write(f"Final Score: {self.scoreboard.score}", align="center", font=("Arial", 18, "normal"))
        
        # Show high score
        high_score_text = Turtle()
        high_score_text.hideturtle()
        high_score_text.penup()
        high_score_text.color("gold")
        high_score_text.goto(0, -30)
        high_score_text.write(f"High Score: {self.scoreboard.high_score}", align="center", font=("Arial", 18, "normal"))
        
        # Restart instruction
        self.restart_text = Turtle()
        self.restart_text.hideturtle()
        self.restart_text.penup()
        self.restart_text.color("white")
        self.restart_text.goto(0, -80)
        self.restart_text.write("Press SPACE to play again", align="center", font=("Arial", 16, "normal"))
        
        self.screen.update()

    def _clear_game_over_screen(self):
        """Clear game over screen objects"""
        # Keep track of game over text objects to clear them properly
        game_over_objects = []
        
        for turtle in self.screen.turtles():
            # Check if this turtle is one of our game over text objects
            if (turtle != self.scoreboard and 
                turtle not in self.snake.segments and 
                turtle != self.food):
                game_over_objects.append(turtle)
        
        # Clear all game over text objects
        for obj in game_over_objects:
            obj.clear()
            obj.hideturtle()

    def _restart_game(self):
        """Restart the game when spacebar is pressed"""
        if self.game_over:
            try:
                self._clear_game_over_screen()
                self.snake.reset()
                self.scoreboard.reset()
                occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}
                self.food.refresh(occupied)
                self.game_over = False
                self.game_is_on = True
            except Exception as e:
                print(f"Error restarting game: {e}")
                # Fallback: try to continue anyway
                self.game_over = False
                self.game_is_on = True

    def run(self):
        """Main game loop"""
        while True:
            if self.game_is_on and not self.game_over:
                self.screen.update()
                time.sleep(self.game_speed)
                
                self.snake.move()
                
                # Check collisions
                self._check_collisions()
            elif self.game_over:
                # Game over state - keep screen responsive for spacebar input
                self.screen.update()
                time.sleep(0.05)  # Small delay to prevent CPU spinning but keep responsive

    def _check_collisions(self):
        """Check all types of collisions"""
        # Check food collision
        if self.snake.head.distance(self.food) < 15:
            self.snake.extend()
            self.scoreboard.increase_score(self.food.points)
            
            # Avoid spawning food inside snake
            occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}
            self.food.refresh(occupied)

        # Check wall collision
        half_w = SCREEN_WIDTH / 2
        half_h = SCREEN_HEIGHT / 2
        x, y = self.snake.head.xcor(), self.snake.head.ycor()
        
        if x > half_w - CELL_SIZE or x < -half_w + CELL_SIZE or y > half_h - CELL_SIZE or y < -half_h + CELL_SIZE:
            self._trigger_game_over()
            return

        # Check self collision
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                self._trigger_game_over()
                break

    def _trigger_game_over(self):
        """Trigger game over state"""
        self.game_over = True
        self.game_is_on = False
        self._show_game_over_screen()


# Main execution
if __name__ == "__main__":
    game = Game()
    game.run()
