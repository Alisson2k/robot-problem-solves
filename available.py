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
        total_path.append(paths)

    return calc_real_path(total_path)

def calc_real_path(paths):
    for i, path in enumerate(paths):
        if i > 0:
            del path[0]

    return [item for sublist in paths for item in sublist]

def get_paths_taken(chromosome: Chromosome, initial: tuple, final: tuple):
    # validar outros movimentos a partir da matrix,
    # como por exemplo o último movimento

    paths = [initial]

    go_on = True
    if PRIORITY_AXIS == Axis.HORIZONTAL:
        if final[1] > initial[1]:
            go_on = _go_right(chromosome, paths, initial, final)
        elif initial[1] > final[1]:
            go_on = _go_up(chromosome, paths, initial, final)

        if go_on:
            initial = paths[len(paths) - 1]

            if final[0] > initial[0]:
                _go_down(chromosome, paths, initial, final)
            elif initial[0] > final[0]:
                _go_left(chromosome, paths, initial, final)
    else:
        if final[0] > initial[0]:
            go_on = _go_down(chromosome, paths, initial, final)
        elif initial[0] > final[0]:
            go_on = _go_left(chromosome, paths, initial, final)

        if go_on:
            initial = paths[len(paths) - 1]

            if final[1] > initial[1]:
                _go_right(chromosome, paths, initial, final)
            elif initial[1] > final[1]:
                _go_up(chromosome, paths, initial, final)

    return paths

def _go_down(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    go_on = True

    for i in range(initial[0] + 1, final[0] + 1):
        path = (i, initial[1])
        paths.append(path)

        if chromosome.matrix.is_can(path) and path != final:
            replace_movement(chromosome, path, final)
            go_on = False
            break

    last_path = paths[len(paths) - 1]
    chromosome.change_robot_position(last_path)
    return go_on

def _go_right(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    go_on = True
    for i in range(initial[1] + 1, final[1] + 1):
        path = (initial[0], i)
        paths.append(path)

        if chromosome.matrix.is_can(path) and path != final:
            replace_movement(chromosome, path, final)
            go_on = False
            break

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)
    return go_on
        
def _go_up(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    go_on = True
    while final[1] != initial[1]:
        initial = (initial[0], initial[1] - 1)
        path = (initial[0], initial[1])
        paths.append(path)

        if chromosome.matrix.is_can(path) and path != final:
            replace_movement(chromosome, path, final)
            go_on = False
            break

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)
    return go_on

def _go_left(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    go_on = True
    while final[0] != initial[0]:
        initial = (initial[0] - 1, initial[1])
        path = (initial[0], initial[1])
        paths.append(path)

        if chromosome.matrix.is_can(path) and path != final:
            replace_movement(chromosome, path, final)
            go_on = False
            break

    last_path = paths[len(paths) - 1]
    chromosome.matrix.content[last_path[0]][last_path[1]] = 0
    chromosome.change_robot_position(last_path)
    return go_on

def replace_movement(chromosome: Chromosome, current: tuple, final: tuple):
    can_index = chromosome.points_sorted.index(current)
    gen_index = chromosome.genes.index(can_index)

    can_index_2 = chromosome.points_sorted.index(final)
    gen_index_2 = chromosome.genes.index(can_index_2)

    chromosome.genes.insert(gen_index_2, can_index)
    del chromosome.genes[gen_index + 1]
