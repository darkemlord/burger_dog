import pygame as pg, random

# Intialize the game
pg.init()

# Set display surface

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Burger Dog")

# Set FPS and clock
FPS = 60
clock = pg.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTING_BURGER_VELOCITY

# Set Colors

ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pg.font.Font("./assets/WashYourHand.ttf", 32)

running = True
# The main game loop
while running:
    # Check if the user quits the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# End game
pg.quit()
