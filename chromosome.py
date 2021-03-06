import copy
import random
from matrix import Matrix

class Chromosome(object):
    def __init__(self, matrix: Matrix):
        self.init_matrix = copy.deepcopy(matrix)
        self.matrix = copy.deepcopy(matrix)
        self.points_sorted = self.matrix.cans_indexed
        self.genes = self._create_genes()
        self.robot_position: tuple = (0, 0)
        self.last_movement: tuple = None

    def reset_chromosome(self):
        self.__init__(self.init_matrix)

    def change_robot_position(self, position: tuple):
        self.matrix.content[self.robot_position[0]][self.robot_position[1]] = 0
        self.robot_position = position
        self.matrix.content[self.robot_position[0]][self.robot_position[1]] = 2

    def _create_genes(self):
        genes = []
        points = random.sample(self.points_sorted, len(self.points_sorted))

        for can in points:
            genes.append(self.points_sorted.index(can))

        return genes

    def __str__(self):
        return str(self.genes)