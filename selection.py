import math
import random
from constants import ROULETE_WHEEL_PERCENT

def roulette_wheel(population: list) -> list:
    size = len(population)
    count = math.ceil(ROULETE_WHEEL_PERCENT * size / 100)

    total = 0
    for pop in population:
        total += len(pop[1])

    total_normalize = 0
    for pop in population:
        total_normalize += total / len(pop[1])

    weights = []
    for pop in population:
        weights.append((total / len(pop[1])) / total_normalize)

    return random.choices(
        population=population,
        weights=weights,
        k=count
    )
