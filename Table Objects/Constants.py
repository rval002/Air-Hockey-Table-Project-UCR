# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Constants used in the Project Such as dimensions.

# **************************************************************************** #


#anything that is zero must still be measured. Dimensional units ???
#Please add any global constants Here.


# ------------- CAMERA -------------
FRAMERATE = 0 # Might be put in with the camera section.

# ------------- START POSITIONS-------------
BORDER_POSITION = (20,150)
PUCK_POSITION = (0,0)
STRIKER_POSITION = (50,220)




# ------------- DIMENSIONS -------------
#  dimensions units
FACE_LENGTH= 600 # 5ft 4 inches (GOAL TO GOAL)
# ScreenWidth = 1200
# ScreenWidth = 610
FACE_WIDTH = 175 # 32 1/2 inches
GOAL_CENTER = 0 #goal to edge is 12 inches
GOAL_SIZE = 0 #goal diamter is 8 inches

# Objects sizes units
PUCK_RADIUS = 14 # 2inches maybe?
STRIKER_RADIUS = 20 # 3 inches maybe?

# -------------- MOTORS --------------
#  limitations
MAX_ACCELERATION = 50
MAX_DECELERATION = 50
MAX_SPEEDX = 50
MAX_SPEEDY = 50


# -------------- COLORS --------------
# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
LIGHT_RED = (200, 150, 150)
DIMMED_RED = (120,60,60)
YELLOW = (255, 255, 0)
DIMMED_YELLOW = (150, 150, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (100, 100, 100)
LIGHT_GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)


# --------------For Pygame Objects Only--------------------------------------
PUCK_COLOR = GREEN
PUCK_TRAJECTORY_COLOR = BLUE
PUCK_PATH_COLOR = RED
STRIKER_COLOR = BLUE
STRIKER_LINE_COLOR = CYAN
BORDER_COLOR = DIMMED_RED
PADDLE_COLOR =ORANGE
