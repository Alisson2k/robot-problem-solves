import copy
from matrix import Matrix
from chromosome import Chromosome
from wrapper_chromosome import Wrapper
from constants import EnumCrossover
from crossover import Crossover
    
class Population(object):

    def __init__(self, matrix: Matrix, size: int, old_population: list = []):
        self.size = size
        self.matrix = matrix
        self.population = old_population
        self._generate_population()

    def _generate_population(self):
        for _ in range(self.size - len(self.population)):
            self.population.append(Wrapper(Chromosome(self.matrix)))

    def get_best(self):
        best = None
        for chromo in self.population:
            if best is None or chromo.distance < best.distance:
                best = chromo

        return best

    def elitism(self, elitism_rate):
        aux_population = copy.deepcopy(self.population)
        aux_population.sort()
        return aux_population[:int(elitism_rate * self.size / 100)]

    def apply_crossover(self, crossover_type):
        news = []
        for j in range(int(len(self.population) / 2)):
            if crossover_type == EnumCrossover.OX:
                new_chromo = Chromosome(self.matrix)
                new_chromo.genes = Crossover.apply_ox(self.population[j].chromosome, self.population[j + 1].chromosome)

                news.append(Wrapper(new_chromo))

        return news

    def __str__(self):
        show = ""
        for i, chromosome in enumerate(self.population):
            show += f'(C #{i}: {chromosome.chromosome}, D: {chromosome.distance})\n'

        return show