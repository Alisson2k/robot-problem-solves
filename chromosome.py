import random
from matrix import Matrix

class Chromosome(object):
    def __init__(self, matrix: Matrix):
        self.matrix = matrix
        self.points_sorted = matrix.cans_indexed
        self.genes = self._create_genes()
        self.robot_position = (0, 0)

    def _create_genes(self):
        genes = []
        points = random.sample(self.points_sorted, len(self.points_sorted))

        for can in points:
            genes.append(self.points_sorted.index(can))

        return genes

    def __str__(self):
        return str(self.genes)