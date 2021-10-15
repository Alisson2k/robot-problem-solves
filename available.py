from chromosome import Chromosome
from constants import Axis, Direction, Wise

class Available(object):
    def __init__(self):
        self.axis_priority = Axis.VERTICAL
        self.wise_priority = Wise.CLOCKWISE
        self.direction_priority = Direction.RIGHT

    def set_default_props(self):
        self.__init__()

    def change_axis_priority(self):
        if self.axis_priority == Axis.VERTICAL:
            self.axis_priority = Axis.HORIZONTAL
        else:
            self.axis_priority = Axis.VERTICAL

av = Available()

def available_chromosome(chromosome: Chromosome):
    av.set_default_props()

    points = []
    for i in range(len(chromosome.genes)):
        points.append(chromosome.points_sorted[chromosome.genes[i]])

    total_path = []
    for gen in chromosome.genes:
        ini = chromosome.robot_position
        fim = chromosome.points_sorted[gen]

        paths = get_paths_taken(chromosome, ini, fim)
        total_path.append(paths)

    return calc_real_path(total_path)

def calc_real_path(paths):
    for path in paths:
        del path[0]

    return [item for sublist in paths for item in sublist]

def get_paths_taken(chromosome: Chromosome, initial: tuple, final: tuple):
    paths = [initial]
    last_movement = chromosome.last_movement

    while True:
        get_paths(paths, chromosome, initial, final)

        if len(paths) > 1 and last_movement == paths[1]:
            paths = [initial]

            if av.axis_priority == Axis.HORIZONTAL and initial[0] != final[0]:
                av.axis_priority = Axis.VERTICAL
            elif av.axis_priority == Axis.VERTICAL and initial[1] != final[1]:
                av.axis_priority = Axis.HORIZONTAL
            else:
                initial = redo_moviment(paths, chromosome, initial, final)
        else:
            break

    return paths

def redo_moviment(paths: list, chromosome: Chromosome, initial: tuple, final: tuple):
    if initial[0] != final[0]:
        av.axis_priority = Axis.VERTICAL

        if av.direction_priority == Direction.RIGHT:
            if initial[1] + 1 < chromosome.matrix.size:
                paths.append((initial[0], initial[1] + 1))
                return (initial[0], initial[1] + 1)
            else:
                paths.append((initial[0], initial[1] - 1))
                return (initial[0], initial[1] - 1)
        else:
            paths.append((initial[0], initial[1] -1))
            return (initial[0], initial[1] - 1)
    else:
        av.axis_priority = Axis.HORIZONTAL
        
        if av.direction_priority == Direction.RIGHT:
            if initial[0] + 1 < chromosome.matrix.size:
                paths.append((initial[0] + 1, initial[1]))
                return (initial[0] + 1, initial[1])
            else:
                paths.append((initial[0] - 1, initial[1]))
                return (initial[0] - 1, initial[1])
        else:
            paths.append((initial[0] - 1, initial[1]))
            return (initial[0] - 1, initial[1])

def get_paths(paths: list, chromosome: Chromosome, initial: tuple, final: tuple):
    go_on = True
    if av.axis_priority == Axis.HORIZONTAL:
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

def _go_down(chromosome: Chromosome, paths, initial: tuple, final: tuple):
    go_on = True

    for i in range(initial[0] + 1, final[0] + 1):
        path = (i, initial[1])
        paths.append(path)

        chromosome.last_movement = paths[len(paths) - 2]

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

        chromosome.last_movement = paths[len(paths) - 2]

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

        chromosome.last_movement = paths[len(paths) - 2]

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

        chromosome.last_movement = paths[len(paths) - 2]

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
