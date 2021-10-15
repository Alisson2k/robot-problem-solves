import random
from chromosome import Chromosome
from matrix import Matrix
from available import available_chromosome

matrix = Matrix(10)
matrix.generate_cans()

chromo = Chromosome(matrix)

def mutation_invert(chromo: Chromosome):
    chromo.genes.reverse()

def mutation_random(genes: list):
    random.shuffle(genes)
