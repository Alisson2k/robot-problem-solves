import random

class Crossover:

    @staticmethod
    def fix_chromosome():
        pass

    @staticmethod
    def apply_ox(chromo1, chromo2, p1 = None, p2 = None):
        size = len(chromo1) - 1

        if p1 is None:
            p1 = random.randint(1, size - 1)
        if p2 is None:
            p2 = random.randint(0, size) 

        start = min(p1, p2)
        end = max(p1, p2)

        child_1 = [None] * (size + 1)
        for i in range(start, end + 1):
            child_1[i] = chromo1[i]

        current_index = 0
        for i in range(size + 1):
            current_index = (end + i) % (size + 1)

            if current_index == start and start != end:
                break
            if current_index == end:
                continue

            j = current_index
            while chromo2[j] in child_1:
                j = (j + 1) % (size + 1)

            child_1[current_index] = chromo2[j]

            if chromo2[j] not in child_1:
                child_1[current_index] = chromo2[j]

        return child_1

    @staticmethod
    def apply_pmx():
        pass

    @staticmethod
    def apply_cx():
        pass
