# Author: 文若
# CreateDate: 2022/6/17
from playLA.Vector import Vector


class Matrix:
    def __init__(self, lst2d):
        self._values = [row[:] for row in lst2d]

    def row_vector(self, index):
        """获得矩阵第index个行向量"""
        # 注意返回的是向量
        return Vector(self._values[index])

    def col_vector(self, index):
        """获得矩阵第index个列向量"""
        # 注意返回的是向量 取出每一行的第index个元素
        return Vector(row[index] for row in self._values)

    def __getitem__(self, pos):
        """获得矩阵某一行某一列的元素 pos元组"""
        r, c = pos
        return self._values[r][c]

    def size(self):
        """返回矩阵元素的个数"""
        r, c = self.shape()
        return r * c

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    """len返回矩阵的行"""
    __len__ = row_num

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状：（行数，列数）"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    # 矩阵运算
    def __add__(self, other):
        """返回两个矩阵的加法运算"""
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])
