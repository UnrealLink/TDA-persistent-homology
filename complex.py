from tqdm import tqdm
from simplex import Simplex
from utils import binary_search

class Complex:
    def __init__(self, filename):
        self.simplices = [] # simplicies sorted by filtration order
        self.lex_simplices = [] # simplices sorted by lexicographic order on vertices
        self.index_map = []

        with open(filename, 'r', encoding='ascii') as f:
            i = 0
            for line in tqdm(f.readlines()):
                simplex = Simplex(*line.split())
                self.lex_simplices.append(simplex)
                self.index_map.append(i)
                i += 1
        self.lex_simplices.sort(key=lambda x: x.vertices)
        self.simplices, self.index_map = zip(*sorted(list(zip(self.lex_simplices, self.index_map)),
                                                     key=lambda x: x[0]))


        for simplex in tqdm(self.simplices):
            simplex.set_faces(self.lex_simplices, self.index_map)
        
        for simplex in self.simplices:
            print(simplex.faces)
