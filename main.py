from matrix import Matrix
from chromosome import Chromosome
from available import available_chromosome

field_size = 5

chromos = []

matrix = Matrix(field_size)
matrix.generate_cans()

chromo = Chromosome(matrix)

# print(matrix.cans_indexed)

available_chromosome(chromo)

# Criar função de avaliação, essa vai modificar o cromossomo, para tornar o caminho válido