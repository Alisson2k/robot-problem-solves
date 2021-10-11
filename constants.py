from enum import Enum

class Axis(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    
class Wise(Enum):
    CLOCKWISE = 0
    COUNTERWISE = 1

class Direction(Enum):
    RIGHT = 0
    LEFT = 1

# percentage of matrix that must be filled by cans
GENERATION_PERCENT = 20

# HORIZONTAL or VERTICAL
PRIORITY_AXIS: Axis = Axis.VERTICAL

# CLOCKWISE OR COUNTERCLOCKWISE
PRIORITY_WISE = Wise.CLOCKWISE

# RIGHT OR LEFT
PRIORITY_DIRECTION = Direction.RIGHT