import copy
import time
from matrix import Matrix
from constants import clear
from chromosome import Chromosome
from wrapper_chromosome import Wrapper

class Visualization(object):

    def __init__(self, matrix: Matrix):
        self._initial_matrix = copy.deepcopy(matrix)
        self.matrix = copy.deepcopy(self._initial_matrix)

    def apply_next_move(self, chromosome: Wrapper, index: int):
        position = chromosome.chromosome.robot_position

        self.matrix.content[position[0]][position[1]] = 0

        chromosome.chromosome.robot_position = chromosome.path[index]
        position = chromosome.chromosome.robot_position

        self.matrix.content[position[0]][position[1]] = 2

    def solution(self, chromosome: Chromosome, delay_in_seconds: int = 0):
        self.__init__(self._initial_matrix)
        chromo = Wrapper(copy.deepcopy(chromosome))
        chromo.chromosome.robot_position = (0, 0)

        clear()
        for total_distance in range(chromo.distance):
            print(f'[*] Distancia percorrida: {total_distance}\n')
            print(self.matrix)

            time.sleep(delay_in_seconds)
            clear()

            self.apply_next_move(chromo, total_distance)

        print(f'[*] Distancia percorrida: {chromo.distance}\n')
        print(self._initial_matrix)
        print()
        print(self.matrix)
