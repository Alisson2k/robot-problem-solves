from enum import Enum

class Axis(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

# percentage of matrix that must be filled by cans
GENERATION_PERCENT = 20

# HORIZONTAL or VERTICAL
PRIORITY_AXIS: Axis = Axis.HORIZONTAL