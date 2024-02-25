import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)

# Set the width and height of the game window
width = 800
height = 600

# Set the size of each grid block
block_size = 20

# Set the initial speed of the snake
snake_speed = 15

# Initialize Pygame
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ultimate Snake Game')

clock = pygame.time.Clock()

font_large = pygame.font.SysFont(None, 80)
font_medium = pygame.font.SysFont(None, 50)
font_small = pygame.font.SysFont(None, 30)

# Load images
apple_img = pygame.image.load('apple.png')
apple_img = pygame.transform.scale(apple_img, (block_size, block_size))

# Functions to display messages and score
def message(msg, color, y_displace=0, font_size=font_medium):
    mesg = font_size.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3 + y_displace])

def score(score):
    value = font_medium.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [10, 10])

# Function to create the snake
def snake(block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(game_display, green, [x, y, block_size, block_size])

# Function to introduce obstacles
def draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height):
    pygame.draw.rect(game_display, purple, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

# Function to display the introduction screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(white)
        message("Welcome to Ultimate Snake Game!", green, -50, font_large)
        message("Eat apples to grow, avoid obstacles", black, 30)
        message("and yourself. Press C to play or Q to quit", yellow, 150, font_medium)
        pygame.display.update()
        clock.tick(15)

    # Add a short delay to give a smooth transition
    pygame.time.delay(500)

# Main game loop
def game_loop():
    game_intro()

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    obstacle_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    obstacle_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
    obstacle_width = 20
    obstacle_height = 60

    while not game_over:

        while game_close:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red, -50, font_large)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        game_display.fill(white)

        draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        game_display.blit(apple_img, (foodx, foody))

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x, y in snake_list[:-1]:
            if x == x1 and y == y1:
                game_close = True

        snake(block_size, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        if (
            x1 < obstacle_x + obstacle_width
            and x1 + block_size > obstacle_x
            and y1 < obstacle_y + obstacle_height
            and y1 + block_size > obstacle_y
        ):
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
