import numpy as np
from tqdm import tqdm
from simplex import Simplex
from column import Column

class Matrix:
    def __init__(self, complex):
        self.pivots = [-1]*len(complex.simplices)
        self.columns = []
        for simplex in tqdm(complex.simplices):
            self.columns.append(Column(simplex))

    def reduction(self):
        for i, column in tqdm(enumerate(self.columns)):
            done = False
            while not done:
                if column.non_zeroes == []:
                    done = True
                else:
                    p = column.non_zeroes[-1]
                    j = self.pivots[p]
                    if j == -1:
                        self.pivots[p] = i
                        done = True
                    else:
                        column += self.columns[j]

    def barcode(self):
        barcode = []
        for i, pivot in enumerate(self.pivots):
            if pivot == -1:
                if self.columns[i].non_zeroes == []:
                    row = self.columns[i].simplex.value
                    barcode.append((self.columns[i].simplex.dim, row, -1))
            else:
                row = self.columns[i].simplex.value
                col = self.columns[pivot].simplex.value
                barcode.append((self.columns[i].simplex.dim, row, col))
        return barcode

    def dense(self):
        dense_mat = np.zeros((len(self.columns), len(self.columns)))
        for i, column in enumerate(self.columns):
            for j in column.non_zeroes:
                dense_mat[j, i] = 1
        return dense_mat

    def __repr__(self):
        return self.dense().__repr__()