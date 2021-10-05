from matrix import Matrix
from chromosome import Chromosome
from constants import Axis, PRIORITY_AXIS

def available_chromosome(chromosome: Chromosome):
    total_path = []

    points = []
    for i in range(len(chromosome.genes)):
        points.append(chromosome.points_sorted[chromosome.genes[i]])

    for gen in chromosome.genes:
        ini = chromosome.robot_position
        fim = chromosome.points_sorted[gen]

        paths = get_paths_taken(chromosome, ini, fim)

        chromosome.robot_position = paths[len(paths) - 1]
        total_path.append(paths)

def get_paths_taken(chromosome: Chromosome, initial: tuple, final: tuple):
    # validar outros movimentos a partir da matrix,
    # como por exemplo o último movimento

    paths = [initial]

    if PRIORITY_AXIS == Axis.HORIZONTAL:
        if final[1] > initial[1]:
            _go_down(chromosome, paths, initial, final)
        elif initial[1] > final[1]:
            _go_up(chromosome, paths, initial, final)

        initial = paths[len(paths) - 1]

        if final[0] > initial[0]:
            _go_right(chromosome, paths, initial, final)
        elif initial[0] > final[0]:
            _go_left(chromosome, paths, initial, final)
    else:
        if final[0] > initial[0]:
            _go_right(chromosome, paths, initial, final)
        elif initial[0] > final[0]:
            _go_left(chromosome, paths, initial, final)

        initial = paths[len(paths) - 1]

        if final[1] > initial[1]:
            _go_down(chromosome, paths, initial, final)
        elif initial[1] > final[1]:
            _go_up(chromosome, paths, initial, final)

    return paths

def _go_down(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    for i in range(initial[1] + 1, final[1] + 1):
        path = (initial[0], i)
        paths.append(path)

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)

def _go_right(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    for i in range(initial[0] + 1, final[0] + 1):
        path = (i, initial[1])
        paths.append(path)

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)
        
def _go_up(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    while final[1] != initial[1]:
        initial = (initial[0], initial[1] - 1)
        path = (initial[0], initial[1])
        paths.append(path)

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)

def _go_left(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    while final[0] != initial[0]:
        initial = (initial[0] - 1, initial[1])
        path = (initial[0], initial[1])
        paths.append(path)

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)
