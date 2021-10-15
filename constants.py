import os
from enum import Enum

clear = lambda: os.system('clear')

class Axis(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    
class Wise(Enum):
    CLOCKWISE = 0
    COUNTERWISE = 1

class Direction(Enum):
    RIGHT = 0
    LEFT = 1

class EnumCrossover(Enum):
    OX = 0
    PMX = 1
    CX = 2

# percentage of matrix that must be filled by cans
GENERATION_PERCENT = 20

# HORIZONTAL or VERTICAL
PRIORITY_AXIS: Axis = Axis.VERTICAL

# CLOCKWISE OR COUNTERCLOCKWISE
PRIORITY_WISE = Wise.CLOCKWISE

# RIGHT OR LEFT
PRIORITY_DIRECTION = Direction.RIGHT

# ROULETE WHEEL PERCENT LIMITATION
ROULETE_WHEEL_PERCENT = 100

# ELITISM RATE (IN PERCENT)
ELITISM_RATE = 10

# CROSSOVER RATE (IN PERCENT)
CROSSOVER_RATE = 15

# MUTATION RATE (IN PERCENT)
MUTATION_RATE = 5