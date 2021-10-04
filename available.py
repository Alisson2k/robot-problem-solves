from matrix import Matrix
from chromosome import Chromosome
from constants import Axis, PRIORITY_AXIS

def available_chromosome(chromosome: Chromosome):
    total_path = []

    for gen in chromosome.genes:
        ini = chromosome.robot_position
        fim = chromosome.points_sorted[gen]

        paths = get_paths_taken(chromosome.matrix, ini, fim)

        chromosome.robot_position = paths[len(paths) - 1]
        total_path.append(paths)

def get_paths_taken(matrix: Matrix, initial: tuple, final: tuple):
    # validar outros movimentos a partir da matrix,
    # como por exemplo o último movimento

    paths = [initial]

    if PRIORITY_AXIS == Axis.HORIZONTAL:
        if final[1] > initial[1]:
            _go_down(paths, initial, final)
        elif initial[1] > final[1]:
            _go_up(paths, initial, final)

        initial = paths[len(paths) - 1]

        if final[0] > initial[0]:
            _go_right(paths, initial, final)
        elif initial[0] > final[0]:
            _go_left(paths, initial, final)
    else:
        if final[0] > initial[0]:
            _go_right(paths, initial, final)
        elif initial[0] > final[0]:
            _go_left(paths, initial, final)

        initial = paths[len(paths) - 1]

        if final[1] > initial[1]:
            _go_down(paths, initial, final)
        elif initial[1] > final[1]:
            _go_up(paths, initial, final)

    return paths

def _go_down(paths, initial: tuple, final: tuple):
    for i in range(initial[1] + 1, final[1] + 1):
        paths.append((initial[0], i))

def _go_right(paths, initial: tuple, final: tuple):
    for i in range(initial[0] + 1, final[0] + 1):
        paths.append((i, initial[1]))
        
def _go_up(paths, initial: tuple, final: tuple):
    while final[1] != initial[1]:
        initial = (initial[0], initial[1] - 1)
        paths.append((initial[0], initial[1]))

def _go_left(paths, initial: tuple, final: tuple):
    while final[0] != initial[0]:
        initial = (initial[0] - 1, initial[1])
        paths.append((initial[0], initial[1]))