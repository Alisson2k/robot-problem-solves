from matrix import Matrix
from chromosome import Chromosome
from available import available_chromosome

class TestPath(object):
    def __init__(self, size):
        self.matrix = Matrix(size)
        self.matrix.generate_cans()

    def test_path_valid(self):
        print("[*] Executing [test_path_valid]")

        chromosome = Chromosome(self.matrix)
        paths = available_chromosome(chromosome)

        for (i, path) in enumerate(paths):
            if i + 2 == len(paths):
                break

            assert path != paths[i + 2]

        for i in range(len(chromosome.matrix.content)):
            for j in range(len(chromosome.matrix.content[0])):
                assert not chromosome.matrix.is_can((i, j))

        assert chromosome.matrix.is_robot(chromosome.robot_position)

        print("[+] Is a valid path!\n")

print("[*] Executing tests...\n")

COUNT = 1

for i in range(COUNT):
    tests = TestPath(50)
    tests.test_path_valid()
