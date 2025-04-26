import pygame
import random
import sys

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))

def random_food():
    return (
        random.randrange(0, WIDTH, GRID_SIZE),
        random.randrange(0, HEIGHT, GRID_SIZE)
    )

def draw_score(screen, font, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food = random_food()
    score = 0
    running = True

    while running:
        clock.tick(10)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
            direction = (0, -GRID_SIZE)
        if keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
            direction = (0, GRID_SIZE)
        if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
            direction = (-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
            direction = (GRID_SIZE, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        if new_head == food:
            food = random_food()
            score += 1
        else:
            snake.pop()

        if (
            new_head in snake[1:] or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

        draw_food(screen, food)
        draw_snake(screen, snake)
        draw_score(screen, font, score)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()