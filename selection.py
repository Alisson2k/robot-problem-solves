import random

def roulette_wheel(population: list) -> list:
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
        k=2
    )
