from random import randrange
from constants import GENERATION_PERCENT

class Matrix(object):
    def __init__(self, size: int, auto_gen_cans: bool = False):
        self.size = size
        self.content = self._init_matrix()
        self.cans = []
        self.cans_indexed = []

        if auto_gen_cans:
            self.generate_cans()

    def _init_matrix(self):
        matrix = [[0 for x in range(self.size)] for y in range(self.size)]
        matrix[0][0] = 2
        return matrix

    def _create_indexed_array(self):
        indexes = []

        for x in range(self.size):
            for y in range(self.size):
                if self.content[x][y] == 1:
                    indexes.append((x, y))

        return indexes

    def generate_cans(self):
        qnt_cans = int(GENERATION_PERCENT * self.size * self.size / 100)
        cans = []

        def _can_place_cans(point):
            can_place = True

            for can in cans:
                if can == point:
                    can_place = False
                    break

            return can_place

        for _ in range(qnt_cans):
            while True:
                x = randrange(self.size)
                y = randrange(self.size)

                if (x != 0 or y != 0) and _can_place_cans((x, y)):
                    self.content[x][y] = 1
                    cans.append((x, y))
                    break

        self.cans = cans
        self.cans_indexed = self._create_indexed_array()

    def is_void(self, position: tuple) -> bool:
        return self.content[position[0]][position[1]] == 0

    def is_can(self, position: tuple) -> bool:
        return self.content[position[0]][position[1]] == 1

    def is_robot(self, position: tuple) -> bool:
        return self.content[position[0]][position[1]] == 2

    def __str__(self):
        return "[ " + ' ]\n[ '.join(['  '.join([str(cell) for cell in row]) for row in self.content]) + " ]"