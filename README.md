# Advanced Snake

Reinterpretation of a well-known arcade game : Snake

**Course**:  PRA2031 - Python Programming Language 

**Date**: P4 2026

**Team Members**: Angela, Noa, Mariyah, Julien, Nicolas, Thijmen & Julie

# Description

## Overview  

There is a snake starting off with zero points in a 2D plane. It will move across a fixed screen and it will eat food, each of which has different points, as the snake hits them, the score on the scoreboard will increase. If the snake collides with itself or an edge the game will restart, this will make the player lose every point they earned and start from scratch. 

## Features

Feature 1 : Snake 

The snake is coded to control its length, as it eats more food the snake will grow longer, it will also code the color of it (grey and blue), how it moves (left, right, up and down) and the movement of the body, this one will follow the path of the head.

Feature 2 : Food. 

States its position : it appears somewhere on the screen and stays there until the snake eats it. 
How it looks : shape, color, the timing of its appearance, random location on the screen.
There are different types of food : red, blue, and gold, each of them corresponds to a different score. 
Red ones count for 1.
Blue for 3. 
Gold for 5.

Feature 3 : Screen.

The screen codes for the size of the platform where the snake moves, and also codes for the scoreboard points. It states when the game needs to restart and when to start again.
Also the color of the screen: What does it look like: black.
Checks for collision, if a collision occurs : game restarts. Self-collision or a collision with the edges. 

## Who is it for?

The game was designed to be accessible to a broad audience. It is simple enough to be used by anyone interested in playing with it. 

## Installation
1. Python SetUp: 
Python served as the primary programming language for implementing the Snake game in this project. A recent version of Python (≥ 3.8) was installed. 
To check if the installation was successful, the following commands were executed in the terminal (PowerShell): python --version  or python3 --version 
To verify that pip (a python package) was also installed, and for these we coded: pip --version or pip3 --version.
2. Project Folder:
To create a new project folder we coded for: cd venv_test and in order to create an isolated virtual environment we typed in the terminal: python -m venv .venv_test This creates a folder containing a self-contained Python environment. To activate the virtual environment: .\.venv_test\Scripts\Activate.ps1
3. Development:
All coding was performed within Visual Studio Code (VS Code), where we implemented GitHub instructions and coded for the three classes chosen for this project: snake, food and screen. To facilitate editing and contribution control, the project repository was cloned from GitHub. This allowed us to do: create a new branch from main for each class/feature and enabled group editing, this was done by coding in the terminal: git add . (prepared / staged the changes), git commit -m  “Add new features” (save the changes with a message describing what you did) and git push (to send my changes to GitHub so everyone can see them)

### Prerequisites 
- Python 3.8 or higher 
- pip (Python package manager)
- Virtual Environment
- GitHub
- VS code

## How to play 
To run the game you must open your terminal: python main.py. You will control the snake with your keyboard pressing the arrow keys (up, down, left or right). The aim of the game is to eat as much food as possible to increase the score. Different types of food will surface and have different score values with predetermined surfacing times to make it a challenge. You will have to avoid touching the edges and your (snake) own body as this ends your game makes you restart the game with 0 points. As the snake eats, its length will grow, making it more difficult to avoid restarting the game again.

# Why did we choose this project ?  

The starting point of the idea to create a game was that all members of this group were beginners in coding. Therefore, we wanted a project that could start very simple, with a functional foundation, but that we could improve depending on our time and capabilities. The aim of this approach was to be sure to be able to deliver a functional project by the end of the project.
Additionally, creating a game sounded like an exciting project, and the prospect of being able to play a game we had built ourselves was motivating.

# What makes it special/different?
This project differes from the original game by the amount of objects involve and the appearances of them

# Limitations and Challenges 

The most difficult : Getting to know the applications (Visual code, Github and python) was a challenge. Being able to program from scratch was the most complicated part of our project.

## Technical limitations?
Challenge 1 : Creating the branches and managing them.
Solution : We realised that we had to create the branches directly on the GitHub repository. And then on VS code, we went into the main branch, and clicked on the origin/ the new branch, and then type on the terminal Git Fetch --all. 

Challenge 2 : Pulling and saving changes 

Solution : Once the changes were done on a branch we saved them and coded on the terminal the following: "git add ." (to prepare the save the changes), "git commint -m "Desired message"" (save the changes with a message) and finally "git push" (to send the changes to GitHub were we could all see the new branch and edit the content of it). Finally to see the changes on visual code, we typed on the terminal "git pull"

Challenge 3 : Connecting the GitHub repository with VS code. 

Solution : To solve this issue we opened VS code and click on the option "Clone Repository". From GitHub, we copy the link to the reporitory of interest and paste it on VS code, the repository must be save in a file in the computer for accesibility. Then the Read.me and LICENCE would show up on the files. 


# Future Improvements 

**Screen** :
- Make the snake move in three dimensions.
- Allow the snake to teleport across the screen.
- Add more obstacles than just the screen edges, obstacles could spawn randomly within the game area.

**Snake** :
- Increase the difficulty by adding a second snake playing at the same time : one snake could be controlled with the left hand, and the other with the right hand.
  
**Food** : 
- Add different types of food with different effects : some could reduce the score, others could modify the snake's apperance (making it shrink or grow). 

# License 

Our project uses the MIT license : 

https://github.com/Thijmen73/advanced-snake/blob/main/LICENSE 

# Contributions

All group members contributed to every aspect of the project, tasks were not divided among us.
