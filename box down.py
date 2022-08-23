# importing gthe required packages
import pygame
import random
import sys
#the programe hich si used every time after importing the packages
pygame.init()

#storing the width and height to the variable which will be use manytime in the programe
WIDTH = 800
HEIGHT = 600

#storing the rgb value to the different variable for color
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR =(0,0,0)

# defining the player size and player position
player_size = 40
player_pos = [WIDTH/2, HEIGHT-player_size]

#defining the enemy size,enemy position and and the list of enemies
enemy_size = 60
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

# defining the speed of the game
SPEED = 10

#this draw the main_window to the screen and set_caption to the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('this is game for noob')

#when the player hit the opponent than this will call to close the game loop
game_over = False

#this store the player score everytime the opponent pass the player it increament to 1
score = 0

#importing the clock function
clock = pygame.time.Clock()

#setting up the font
myFont = pygame.font.SysFont("monospace", 35)


# making a function set_lvl which increases the speed of the game according to the increament in speed
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
	# SPEED = score/5 + 1

# making a function which draws enemies
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
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

			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)

	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()