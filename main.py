import random
from matrix import Matrix
from population import Population
from constants import EnumCrossover, ELITISM_RATE, MUTATION_RATE
from selection import roulette_wheel

SIZE = 50
QNT_POPULATION = 10
EPOCHS = 50

matrix = Matrix(SIZE)
matrix.generate_cans()

print(matrix)
print()

population = Population(matrix, QNT_POPULATION)
# print(population)

def flatten(population, to_append):
    for sublist in to_append:
        population.append(sublist)

for i in range(EPOCHS):
    new_population = []
    
    bests = population.elitism(ELITISM_RATE)
    
    selected = roulette_wheel(population)

    news = population.apply_crossover(EnumCrossover.OX)
    
    # if random.randint(0, 100) < MUTATION_RATE:
    #     population.apply_mutation()

    flatten(new_population, selected)
    flatten(new_population, news)

    new_population = random.choices(population=new_population, k=QNT_POPULATION - len(bests))
    flatten(new_population, bests)

    population = Population(matrix, QNT_POPULATION, new_population)

best = population.get_best() 
print(best)
# print(best.path)