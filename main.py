from complex import Complex
from simplex import Simplex
from column import Column
from matrix import Matrix

if __name__ == "__main__":
    print("Parsing data...")
    complex = Complex("data/filtration_B.txt")
    # print(complex)
    print("Creating boundary matrix...")
    matrix = Matrix(complex)
    # print(matrix)
    print("Matrix reduction...")
    matrix.reduction()
    # print(matrix)
    barcode = matrix.barcode()
    print(barcode)

