from available import available_chromosome

class Wrapper(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.path = available_chromosome(self.chromosome)
        self.distance = len(self.path)

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return f'(C: {self.chromosome}, D: {self.distance})'