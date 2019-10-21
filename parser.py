from tqdm import tqdm

from simplex import Simplex
from column import Column
from matrix import Matrix

def parse_file(filename):
    complex = []
    with open(filename, 'r', encoding='ascii') as f:
        for line in tqdm(f.readlines()):
            complex.append(Simplex(*line.split()))
    complex.sort()
    for simplex in tqdm(complex):
        simplex.set_faces(complex)
    return complex

if __name__ == "__main__":
    print("Parsing data...")
    complex = parse_file("data/test.txt")
    # print(complex)
    print("Creating boundary matrix...")
    matrix = Matrix(complex)
    # print(matrix)
    print("Matrix reduction...")
    matrix.reduction()
    # print(matrix)
    barcode = matrix.barcode()
    print(barcode)

