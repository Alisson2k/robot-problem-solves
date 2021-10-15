import random
from matrix import Matrix
from population import Population
from selection import roulette_wheel
from crossover import Crossover
from wrapper_chromosome import Wrapper
from mutation import mutation_invert, mutation_random

def flatten(population, to_append):
    for sublist in to_append:
        population.append(sublist)

# Tamanho do problema (matrix)
MATRIX_SIZE = 25

# Tamanho da população
POPULATION_SIZE = 50

# Quantidade de gerações
NUMBER_OF_GENERATIONS = 50

# Chance de mutação
MUTATION_RATE = 5

# Taxa de elitismo
ELITISM_RATE = 20


# Gera uma matriz inicial
matrix = Matrix(MATRIX_SIZE, True)

# Gera uma população incial aleatória
population = Population(matrix, POPULATION_SIZE)
print(f'[*] Inicialmente: {population.get_best().distance}\n')
print(matrix)
print()

# Inicia a seleção natural
for i in range(NUMBER_OF_GENERATIONS):
    # Array para próxima geracao
    next_population = []

    # Seleciona os melhores, elitismo
    bests = population.elitism(ELITISM_RATE)

    # Joga os melhores na proxima geracao
    flatten(next_population, bests)

    # Até preencher todos os "POPULATION_SIZE", seleciona
    # dois individuos para fazer crossover
    # gera um novo, e talvez aplica uma mutacao no gerado
    while len(next_population) != POPULATION_SIZE:
        parents = roulette_wheel(population)
        child = Crossover.apply_ox(parents[0].chromosome, parents[1].chromosome)

        if random.randint(0, 100) < MUTATION_RATE:
            # mutation_random(child)
            mutation_invert(child)

        next_population.append(Wrapper(child))

    population = Population(matrix, POPULATION_SIZE, next_population)
    print(f'[{i}] Distancia: {population.get_best().distance}')
