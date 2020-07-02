import os
import glob
from matrix import Matrix


def write_matrix(mat, filepath):
    fpath = os.path.dirname(filepath)
    try:
        if not os.path.exists(fpath):
            os.makedirs(os.path.join(fpath))
    except FileExistsError as e:
        print(e)

    with open(filepath, "w") as f:
        f.write(f"{mat}")

def read_matrix(filepath):
    with open(filepath, "r") as f:
        matrix = f.read()
    matrix = eval(matrix)
    matrix = Matrix(matrix)
    return matrix


def read_all_matrices(dirpath):
    matrix = []
    mat_path = os.path.join(dirpath, "*.mat")
    mat_file_list = glob.glob(mat_path)
    for mat_file in mat_file_list:
        temp = read_matrix(mat_file)
        matrix.append(temp)
    return matrix

