from matrix import Matrix
from chromosome import Chromosome
from crossover import Crossover

class TestCrossover(object):

    def __init__(self, size):
        self.size = size
        self.matrix = Matrix(size)
        self.matrix.generate_cans()

    def test_ox(self):
        print("[*] Executing [test_ox]")
        
        c1 = Chromosome(self.matrix)
        c2 = Chromosome(self.matrix)

        p1 = self.size - 6
        p2 = self.size - 3

        res = Crossover.apply_ox(c1, c2, p1, p2)

        assert res.genes[p1:p2] == c1.genes[p1:p2]
        assert list(dict.fromkeys(res.genes)) == res.genes

        print("[+] OX crossover is applied!\n")

print("[*] Executing tests...\n")

COUNT = 1
SIZE = 10

assert SIZE > 6

for i in range(COUNT):
    tests = TestCrossover(10)
    tests.test_ox()
