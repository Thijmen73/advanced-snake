from __future__ import annotations
import time
import random
import turtle
from turtle import Screen
from snake import Snake, STARTING_POSITIONS, UP, DOWN, LEFT, RIGHT, MOVE_DISTANCE
from food import Food
from screen import Scoreboard, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

# Game class (runner)
class Game:
    def __init__(self):
        # Screen setup
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Advanced Snake Game")
        self.screen.tracer(0)

        # Create objects from old files
        self.snake = Snake()
        self.food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.scoreboard = Scoreboard()

        # Controls
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self._restart_game, "space")  # Spacebar to restart

        # Game state
        self.game_speed = 0.1
        self.game_is_on = True
        self.game_over = False
        
        # Stats
        self.food_eaten = 0
        self.total_movement = 0
        self.start_time = time.time()
        
        # game over screen objects
        self.game_over_text = None
        self.restart_text = None

    def run(self) -> None:
        """Main game loop"""
        try:
            while True:
                if self.game_is_on and not self.game_over:
                    self.screen.update()
                    time.sleep(self.game_speed)

                    # move snake and track movement
                    self.snake.move()
                    self.total_movement += MOVE_DISTANCE

                    # check all collisions
                    self._check_collisions()
                elif self.game_over:
                    # Game over state - wait for spacebar
                    self.screen.update()
                    time.sleep(0.05)  # Small delay to prevent CPU spinning but keep responsive
        except turtle.Terminator:
            # Handle window close gracefully
            print("Game closed by user")
        except Exception as e:
            print(f"Game error: {e}")
        finally:
            # Clean up
            try:
                self.screen.bye()
            except:
                pass

    def _check_collisions(self) -> None:
        """Check all types of collisions"""
        self._check_food_collision()
        self._check_wall_collision()
        self._check_self_collision()

    def _check_food_collision(self) -> None:
        """Check if snake eats food"""
        if self.snake.head.distance(self.food) < 15:
            self.snake.extend()
            self.scoreboard.increase_score(self.food.points)
            self.food_eaten += 1

            # avoid spawning food inside snake
            occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}
            self.food.refresh(occupied)

    def _check_wall_collision(self) -> None:
        """Check if snake hits walls"""
        half_w = SCREEN_WIDTH / 2
        half_h = SCREEN_HEIGHT / 2
        x, y = self.snake.head.xcor(), self.snake.head.ycor()

        if x > half_w - CELL_SIZE or x < -half_w + CELL_SIZE or y > half_h - CELL_SIZE or y < -half_h + CELL_SIZE:
            self._trigger_game_over()

    def _check_self_collision(self) -> None:
        """Check if snake hits itself"""
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                self._trigger_game_over()
                break

    def _show_game_over_screen(self):
        """Display game over screen with leaderboard"""
        from turtle import Turtle
        
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
        try:
            # Clear specific game over text objects if they exist
            if hasattr(self, 'game_over_text') and self.game_over_text:
                self.game_over_text.clear()
                self.game_over_text.hideturtle()
                self.game_over_text = None
                
            if hasattr(self, 'restart_text') and self.restart_text:
                self.restart_text.clear()
                self.restart_text.hideturtle()
                self.restart_text = None
                
            # Clear any other text turtles that might be game over related
            for turtle in self.screen.turtles():
                if (turtle != self.scoreboard and 
                    turtle not in self.snake.segments and 
                    turtle != self.food):
                    turtle.clear()
                    turtle.hideturtle()
        except Exception as e:
            print(f"Error clearing game over screen: {e}")
            pass

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
                
                # Reset stats
                self.food_eaten = 0
                self.total_movement = 0
                self.start_time = time.time()
            except Exception as e:
                print(f"Error restarting game: {e}")
                # Fallback: try to continue anyway
                self.game_over = False
                self.game_is_on = True

    def _trigger_game_over(self):
        """Trigger game over state"""
        if not self.game_over:  # Only trigger if not already game over
            self.game_over = True
            self.game_is_on = False
            self._show_game_over_screen()


# Run the beautiful game
if __name__ == "__main__":
    game = Game()
    game.run()
