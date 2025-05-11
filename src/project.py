import pygame
import random
import sys


WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food(screen, food_list):
    for food in food_list:
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))

def random_food():
    return (
        random.randrange(0, WIDTH, GRID_SIZE),
        random.randrange(0, HEIGHT, GRID_SIZE)
    )

def draw_score(screen, font, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def show_game_over(screen, font, score):
    screen.fill(BLACK)
    msg1 = font.render("Game Over!", True, RED)
    msg2 = font.render(f"Final Score: {score}", True, WHITE)
    msg3 = font.render("Press R to Restart or Q to Quit", True, WHITE)
    
    screen.blit(msg1, (WIDTH//2 - msg1.get_width()//2, HEIGHT//2 - 60))
    screen.blit(msg2, (WIDTH//2 - msg2.get_width()//2, HEIGHT//2 - 20))
    screen.blit(msg3, (WIDTH//2 - msg3.get_width()//2, HEIGHT//2 + 20))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smooth Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food_list = [random_food() for _ in range(3)]
    score = 0

    snake_speed = 120 
    last_move_time = pygame.time.get_ticks()

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
            direction = (0, -GRID_SIZE)
        elif keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
            direction = (0, GRID_SIZE)
        elif keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
            direction = (-GRID_SIZE, 0)
        elif keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
            direction = (GRID_SIZE, 0)

        if current_time - last_move_time > snake_speed:
            last_move_time = current_time
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            snake.insert(0, new_head)

            for i, food in enumerate(food_list):
                if new_head == food:
                    food_list[i] = random_food()
                    score += 1
                    break
            else:
                snake.pop()


            if (
                new_head in snake[1:] or
                new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT
            ):
                show_game_over(screen, font, score)
                running = False

        draw_food(screen, food_list)
        draw_snake(screen, snake)
        draw_score(screen, font, score)
        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("game_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while True:
        run_game()


if __name__ == "__main__":
    main()
