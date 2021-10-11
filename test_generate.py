from matrix import Matrix
from chromosome import Chromosome
from constants import GENERATION_PERCENT

def list_has_duplicated(array):
    return list(dict.fromkeys(array)) == array

class TestGenerate(object):
    def __init__(self, size):
        self.size = size
        self.matrix = Matrix(size)
        self.chromosome = None

    def test_matrix(self):
        print("[*] Executing [test_matrix]")
        
        assert len(self.matrix.content) == self.size

        for i in range(self.size):
            assert len(self.matrix.content[i]) == self.size

        print("[+] Matrix creation ok!\n")

    def test_cans(self):
        print("[*] Executing [test_cans]")
        assert len(self.matrix.cans) == 0

        self.matrix.generate_cans()

        assert len(self.matrix.cans) == int(GENERATION_PERCENT * self.size * self.size / 100)

        for can in self.matrix.cans:
            assert can[0] != 0 or can[1] != 0

        assert list_has_duplicated(self.matrix.cans)

        print("[+] Cans generation are all ok!\n")

    def test_chromosome(self):
        print("[*] Executing [test_chromosome]")

        assert self.chromosome == None

        self.chromosome = Chromosome(self.matrix)

        assert len(self.chromosome.genes) == len(self.matrix.cans)
        assert len(self.chromosome.points_sorted) == len(self.matrix.cans)

        for point in self.chromosome.points_sorted:
            assert point[0] != 0 or point[1] != 0

        assert list_has_duplicated(self.chromosome.points_sorted)
        assert list_has_duplicated(self.chromosome.genes)

        new_chromo = Chromosome(self.matrix)
        assert new_chromo.genes != self.chromosome.genes

        print("[+] Chromosome created and it is valid!\n")

print("[*] Executing tests...\n")

COUNT = 1

for i in range(COUNT):
    tests = TestGenerate(10)
    tests.test_matrix()
    tests.test_cans()
    tests.test_chromosome()