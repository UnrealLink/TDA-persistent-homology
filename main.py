import pickle
from complex import Complex
from simplex import Simplex
from column import Column
from matrix import Matrix
from plot import plot_barcode


INPUT_FILE = "moebius"

if __name__ == "__main__":
    print("Parsing data...")
    complex = Complex(f"data/{INPUT_FILE}.txt")
    # print(complex)
    print("Creating boundary matrix...")
    matrix = Matrix(complex)
    # print(matrix)
    print("Matrix reduction...")
    matrix.reduction()
    # print(matrix)
    print("Computing barcode...")
    barcode = matrix.barcode()
    with open(f'results/result_{INPUT_FILE}.pickled', 'wb') as f:
        pickle.dump(barcode, f)
    with open(f'results/result_{INPUT_FILE}.txt', 'w') as f:
        for code in barcode:
            f.write("{} {} {}\n".format(*code))
    # print(barcode)
    # with open(f'results/result_{INPUT_FILE}.pickled', 'rb') as f:
    #     barcode = pickle.load(f)
    plot_barcode(barcode, min_length=0., arrow_size=1)

