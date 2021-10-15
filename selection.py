import math
import random
from constants import ROULETE_WHEEL_PERCENT

def roulette_wheel(population: list) -> list:
    size = len(population.population)
    count = math.ceil(ROULETE_WHEEL_PERCENT * size / 100)

    total = 0
    for pop in population.population:
        total += pop.distance

    total_normalize = 0
    for pop in population.population:
        total_normalize += total / pop.distance

    weights = []
    for pop in population.population:
        weights.append((total / pop.distance) / total_normalize)

    return random.choices(
        population=population.population,
        weights=weights,
        k=count
    )
