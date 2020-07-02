import os
import shutil
from matrix import Matrix
import matrix_file as mf


def test_matrix():
    test_row_size_error()
    test_add_size_error()
    test_mul_size_error()
    test_add_result()
    test_mul_result()
    test_read_write()
    test_write_anywhere()
    # 테스트 케이스 +
    test_power()
    test_sqrt()
    test_sum(axis=1)
    test_concatenate(axis=1)

def test_row_size_error():
    print("test_row_size_error: 각 행의 길이 검사를 하는지 확인")
    t1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    t2 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    t3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
    t4 = [[1, 2], [5, 6, 7], [9, 10, 11, 12]]

    def create_mat(data):
        m = Matrix(data)

    create_mat(t1)
    create_mat(t2)

    supposed_to_make_error(create_mat, t3)
    supposed_to_make_error(create_mat, t4)
    print("!!! test_row_size_error passed")


def test_add_size_error():
    print("test_add_size_error: 두 행렬이 더해질 수 있는 크기의 행렬인지 확인하는지를 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    m2 = Matrix([[9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]])
    m3 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    m4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


    def add_mat(ma, mb):
        mat = ma + mb

    add_mat(m1, m1)
    add_mat(m1, m2)

    supposed_to_make_error(add_mat, m1, m3)
    supposed_to_make_error(add_mat, m1, m4)
    supposed_to_make_error(add_mat, m2, m4)
    print("!!! test_add_size_error passed")


def test_mul_size_error():
    print("test_mul_size_error: 두 행렬이 곱해질 수 있는 크기의 행렬인지 확인하는지를 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])

    def mul_mat(ma, mb):
        mat = ma * mb

    mul_mat(m1, m2)
    mul_mat(m3, m3)

    supposed_to_make_error(mul_mat, m1, m3)
    supposed_to_make_error(mul_mat, m2, m4)
    supposed_to_make_error(mul_mat, m3, m4)
    print("!!! test_mul_size_error passed")


def test_add_result():
    print("test_add_result: 두 행렬을 더한 값이 맞는지 확인")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    m3 = m1 + m2

    assert m3.data == [[2, 4], [6, 8]]

    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    m2 = Matrix([[1, 3, 5, 7], [2, 4, 6, 8], [9, 10, 11, 12]])
    m3 = m1 + m2

    assert m3.data == [[2, 5, 8, 11], [7, 10, 13, 16], [18, 20, 22, 24]]
    print("!!! test_add_result_passed")


def test_mul_result():
    print("test_mul_result: 두 행렬을 곱한 값이 맞는지 확인")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    m3 = m1 * m2

    assert m3.data == [[7, 10], [15, 22]]

    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    m2 = Matrix([[1, 3, 5], [7, 2, 4], [6, 8, 9], [10, 11, 12]])
    m3 = m1 * m2

    assert m3.data == [[73, 75, 88], [169, 171, 208], [265, 267, 328]]
    print("!!! test_mul_result_passed")


def test_read_write():
    print("test_read_write: 행렬을 파일출력 후 다시 읽었을때 같은 값의 행렬이 나오는지 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    m2 = Matrix([[1, 3, 5], [7, 2, 4], [6, 8, 9], [10, 11, 12]])
    m3 = m1 * m2

    savedir = os.path.dirname(os.path.abspath(__file__))
    mf.write_matrix(m1, os.path.join(savedir, "m1.mat"))
    mf.write_matrix(m2, os.path.join(savedir, "m2.mat"))
    mf.write_matrix(m3, os.path.join(savedir, "m3.mat"))

    m1_read = mf.read_matrix(os.path.join(savedir, "m1.mat"))
    assert m1.data == m1_read.data

    mats = mf.read_all_matrices(savedir)
    assert m2.data == mats[1].data
    assert m3.data == mats[2].data
    print("!!! test_read_write passed")


def test_write_anywhere():
    print("test_write_anywhere: 행렬을 임의의 경로에 만들 수 있는지 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    savedir = "C:\\mat987\\data135"
    shutil.rmtree(savedir, ignore_errors=True)
    mf.write_matrix(m1, os.path.join(savedir, "m1.mat"))
    print("!!! test_write_anywhere passed")


def supposed_to_make_error(func, *args):
    try:
        func(*args)
    except ValueError as ve:
        print(ve)

        return
    assert False


def test_power():
    print("test_power: power 연산확인")
    m1 = Matrix([[9, 3, 2], [1, 3, 9], [1, 6, 8]])
    m2 = Matrix([[1, 4, 2], [3, 3, 4], [2, 1, 3]])

    def power(m1, m2):
        matrix = [[mele ** ele for mele, ele in zip(mrow, row)] for mrow, row in zip(m1.data, m2.data)]
    power(m1, m2)
    print("!!! test_power passed")

def test_sqrt():
    print("test_sqrt: sqrt 연산 확인")
    m1 = Matrix([[0.11, 0.07, 0.29], [0.75, 0.93, 0.54], [0.28, 0.67, 0.49]])

    def sqrt(m1):
        matrix = [[ele**0.5 for ele in row] for row in m1.data]
    sqrt(m1)
    print("!!! test_sqrt passed")

def test_sum(axis=None):
    print("test_sum: sum 연산 확인")
    m1 = Matrix([[1, 2], [5, 6], [9, 10]])

    def sum_matrix(m1, axis):
        if axis == 0:
            result = []
            for col in range(m1.cols):
                temp = 0
                for row in range(m1.rows):
                    temp += m1.data[row][col]
                result.append(temp)

        elif axis == 1:
            result = []
            for row in range(m1.rows):
                temp = 0
                for col in range(m1.cols):
                    temp += m1.data[row][col]
                result.append(temp)

        else:
            result = 0
            for row in m1.data:
                for ele in row:
                    result += ele

    sum_matrix(m1, axis)
    print("!!! test_sum passed")

def test_concatenate(axis=None):
    print("test_concatenate: concatenate 연산 확인")
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[3, 4, 5], [6, 7, 8], [9, 10, 11]])

    def concatenate_matrix(m1, m2, axis):
        if axis == 0:
            temp1 = [row for row in m1.data]
            temp2 = [row for row in m2.data]
            result = temp1 + temp2

        elif axis == 1:
            temp1 = [row for row in m1.data]
            temp2 = [row for row in m2.data]
            result = [temp1[row] + temp2[row] for row in range(m1.rows)]

        else:
            temp1 = [ele for row in m1.data for ele in row]
            temp2 = [ele for row in m2.data for ele in row]
            result = temp1 + temp2

    concatenate_matrix(m1, m2, axis)
    print("!!! test_concatenate passed")

if __name__ == "__main__":
    test_matrix()
