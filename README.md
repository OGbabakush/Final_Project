# Smooth Snake Game

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: (https://github.com/OGbabakush/Final_Project.git)

## Description
This project is a modern take on the classic Snake game, developed using Python and the Pygame library. The player controls a green snake that grows longer each time it eats food, which is randomly spawned across the screen. Unlike the traditional version, this game features multiple food items, smooth animation, and background music to enhance the overall experience. The game continues until the snake collides with the wall or itself, after which the player is given the option to restart or quit.

`project.py`: The main Python script containing the entire game logic. It includes functions for drawing the snake and food, handling movement and collisions, keeping score, managing game states (running/game over), and playing music.
`game_music.mp3`: The background music file that plays in a continuous loop while the game is running. This adds an immersive audio layer to the gameplay.

The game is built around a grid-based movement system with a fixed-size screen. The use of `GRID_SIZE` ensures consistent movement and simplifies food placement. The decision to support multiple food items increases the pace of gameplay.

To keep the visual style simple and clean, only basic colored shapes are used. Audio is handled through Pygame’s `mixer` module, with low-volume background music that adds atmosphere without distracting the player.

Smooth movement is achieved using a timed update loop instead of relying on the frame rate, which helps ensure consistent snake speed regardless of system performance.

This Snake game demonstrates the fundamentals of game development using Python and Pygame, while also showcasing interactive design skills. It is simple, functional, and fun to play, and leaves plenty of room for future creativity and enhancements. It serves as a solid foundation for exploring deeper areas of media and digital arts through coding, sound, and game design.

### Tutorials I used:
* https://youtu.be/PSFM8-byvAE
* https://youtu.be/FtqWCo1_I4g
