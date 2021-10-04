from matrix import Matrix
from chromosome import Chromosome
from constants import Axis, PRIORITY_AXIS

def available_chromosome(matrix: Matrix, chromosome: Chromosome):
    # estou na posicao 0, 0
    get_paths_taken(matrix, (0, 0), (3, 3))

    print("retorna o cromossomo avaliado")
    print(matrix)
    print(chromosome)

def get_paths_taken(matrix: Matrix, initial: tuple, final: tuple):
    # vertical => initial[0] | final[0]
    # horizontal => initial[1] | final[1]

    paths = [initial]

    print(initial, final)

    if PRIORITY_AXIS == Axis.VERTICAL:
        for i in range(initial[0] + 1, final[0] + 1):
            paths.append((i, initial[1]))

        initial = paths[len(paths) - 1]

        for i in range(initial[1] + 1, final[1] + 1):
            paths.append((i, initial[0]))
    else:
        for i in range(initial[1] + 1, final[1] + 1):
            paths.append((initial[0], i))

        initial = paths[len(paths) - 1]

        for i in range(initial[0] + 1, final[0] + 1):
            paths.append((i, initial[1]))

    print(paths)
