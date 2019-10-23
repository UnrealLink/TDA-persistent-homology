from tqdm import tqdm
from multiprocessing import Pool
from time import time
from simplex import Simplex
from utils import binary_search

class Complex:
    def __init__(self, filename):
        self.simplices = [] # simplicies sorted by filtration order
        self.lex_simplices = [] # simplices sorted by lexicographic order on vertices
        self.index_map = []

        with open(filename, 'r', encoding='ascii') as f:
            for line in tqdm(f.readlines()):
                simplex = Simplex(*line.split())
                self.lex_simplices.append(simplex)
        self.index_map = list(range(len(self.lex_simplices)))
        self.lex_simplices.sort(key=lambda x: x.vertices) # sort simplices by lexicographical order on the sorted vertices
        # this sort the simplices by the filtration order, and keep the indexes of the simplices per the list above
        self.simplices, self.index_map = zip(*sorted(list(zip(self.lex_simplices, self.index_map)),
                                                     key=lambda x: x[0]))

        pool = Pool() # using multiprocessing to gain some time
        start = time()
        print("Computing faces... (no progress bar available, this might take a few minutes)", end="")
        self.simplices = pool.map(self.set_faces, self.simplices)
        pool.close()
        self.simplices.sort()
        print(f" Done in {time()-start} s")

        # for simplex in tqdm(self.simplices):
        #     simplex.set_faces(self.lex_simplices, self.index_map)

    def set_faces(self, simplex):
        simplex.set_faces(self.lex_simplices, self.index_map)
        return simplex # child process has a copy of simplex so modifying in place doesn't work
