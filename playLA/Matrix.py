# Author: 文若
# CreateDate: 2022/6/17
class Matrix:
    def __init__(self, lst2d):
        self._values = [row[:] for row in lst2d]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__
