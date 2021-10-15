import random
from chromosome import Chromosome

def mutation_invert(chromo: Chromosome):
    chromo.genes.reverse()

def mutation_random(chromo: Chromosome):
    random.shuffle(chromo.genes)
