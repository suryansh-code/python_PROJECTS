import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Player
player_size = 40
player_pos = [WIDTH / 2, HEIGHT - player_size]

# Load the player image
playero = pygame.image.load('mario.png')
player_image = pygame.transform.scale(playero, (player_size, player_size))

# Enemies
enemy_size = 60
enemy_images = []  # List to store enemy images

# Load enemy images (you can add multiple enemy images)
e1 = pygame.image.load('e1.png')
e2 = pygame.image.load('e2.png')

desired_width = 100
desired_height = 100

e1_resized = pygame.transform.scale(e1, (desired_width, desired_height))
e2_resized = pygame.transform.scale(e2, (desired_width, desired_height))

# Initialize position for drawing the resized image
image_x = (WIDTH - desired_width) // 2
image_y = (HEIGHT - desired_height) // 2

# Enemy list (now it will store both enemy positions and their corresponding images)
enemy_list = []

# Game Speed
SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('This is a game for noob')

# Load the background image
background_image = pygame.image.load('14966453.jpg')

# When the player hits the opponent, this will call to close the game loop
game_over = False

# This stores the player's score; every time the opponent passes the player, it increments by 1
score = 0

# Import the clock function
clock = pygame.time.Clock()

# Setting up the font
myFont = pygame.font.SysFont("monospace", 35)

# Making a function to set the level, which increases the speed of the game according to the score
def set_level(score, SPEED):
    if score < 20:
        SPEED = 10
    elif score < 40:
        SPEED = 10
    elif score < 60:
        SPEED = 20
    else:
        SPEED = 20
    return SPEED

# Making a function to draw enemies
def draw_enemies(enemy_list):
    for enemy_info in enemy_list:
        enemy_x, enemy_y, enemy_image = enemy_info
        screen.blit(enemy_image, (enemy_x, enemy_y))  # Draw the enemy image

# Making a function to drop enemies
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_image = random.choice([e1_resized, e2_resized])
        enemy_list.append([x_pos, y_pos, enemy_image])

# Making a function to update enemy positions
def update_enemy_positions(enemy_list, score):
    for idx, enemy_info in enumerate(enemy_list):
        enemy_x, enemy_y, enemy_image = enemy_info
        if enemy_y >= 0 and enemy_y < HEIGHT:
            enemy_y += SPEED
            enemy_info[1] = enemy_y
        else:
            enemy_list.pop(idx)
            score += 1
    return score

# Making a function to check for collisions
def collision_check(enemy_list, player_pos):
    for enemy_info in enemy_list:
        enemy_x, enemy_y, _ = enemy_info
        if player_pos[0] < enemy_x + enemy_size and player_pos[0] + player_size > enemy_x and \
           player_pos[1] < enemy_y + enemy_size and player_pos[1] + player_size > enemy_y:
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x, y]

    screen.blit(background_image, (0, 0))

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    # Draw the player and enemies
    screen.blit(player_image, (player_pos[0], player_pos[1]))
    draw_enemies(enemy_list)  # Draw the enemies

    clock.tick(30)

    pygame.display.update()
