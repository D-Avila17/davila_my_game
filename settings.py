# File created by: Diego Avila

# screen dimensions
WIDTH = 800
HEIGHT = 600

# game settings
FPS = 30
RUNNING = True
SCORE = 0
PAUSED = False

# player attributes
PLAYER_ACC = 2
MOB_ACC = 2

PLAYER_FRICTION = -0.12
MOB_FRICTION = -0.12
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
# colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncy"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (200,200,200), "normal")]