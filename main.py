import time
import random
from matrix import Matrix
from population import Population
from selection import roulette_wheel
from crossover import Crossover
from wrapper_chromosome import Wrapper
from mutation import mutation_invert
from utils import read_matrix_by_file
from visualization import Visualization

def flatten(population, to_append):
    for sublist in to_append:
        population.append(sublist)

# Tamanho do problema (matrix)
MATRIX_SIZE = 20

# Tamanho da população
POPULATION_SIZE = 20

# Quantidade de gerações
NUMBER_OF_GENERATIONS = 500

# Chance de mutação
MUTATION_RATE = 10

# Taxa de elitismo
ELITISM_RATE = 25


# Gera uma matriz inicial
matrix = Matrix(MATRIX_SIZE, True)
# matrix = read_matrix_by_file('example.txt')

def resolve():
    population = Population(matrix, POPULATION_SIZE)
    print(f'[*] Inicialmente: {population.get_best().distance}\n')
    print(matrix)
    print()

    # view = Visualization(matrix)
    # view.solution(population.get_best(), 0.2)

    for i in range(NUMBER_OF_GENERATIONS):
        next_population = []

        bests = population.elitism(ELITISM_RATE)

        flatten(next_population, bests)

        while len(next_population) != POPULATION_SIZE:
            parents = roulette_wheel(population)
            child = Crossover.apply_ox(parents[0].chromosome, parents[1].chromosome)

            if random.randint(0, 100) < MUTATION_RATE:
                mutation_invert(child)

            next_population.append(Wrapper(child))

        population = Population(matrix, POPULATION_SIZE, next_population)
        print(f'[{i}] Distancia: {population.get_best().distance}')

    return population

now = time.time()
best_solution = resolve().get_best()

print()
print(best_solution.path)
print(f'\n[+] Levou cerca de: {(time.time() - now):.2f}s')

input("Pressione Enter para visualizar a solucao...")

view = Visualization(matrix)
view.solution(best_solution, 0.2)
