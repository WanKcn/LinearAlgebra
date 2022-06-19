# Author: 文若 
# CreateDate: 2022/6/17
from playLA.Matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)

    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.row = {}".format(matrix.row_num()))
    print("matrix.col = {}".format(matrix.col_num()))
    print("matrix.size = {}".format(matrix.size()))

    # 获得某一行某一列的元素
    print("matrix[0][2] = {}".format(matrix[0, 2]))

    print(matrix.row_vector(0))
    print(matrix.col_vector(1))  # 2,5,8
