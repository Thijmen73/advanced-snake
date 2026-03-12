#!/usr/bin/env python3
"""
Main entry point for the Advanced Snake Game
Run this file to start the game with persistent leaderboard and game over screen
"""

from screen import Game

if __name__ == "__main__":
    print("Starting Advanced Snake Game...")
    print("Use arrow keys to move the snake")
    print("Press SPACE to restart after game over")
    print("High scores will be saved automatically")
    
    game = Game()
    game.run()
