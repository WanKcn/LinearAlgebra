class Vector:
    """
    数学类设计为不可更改的类，向量类对象在进行运算时，不对类内的值进行修改，将运算结果以新对象返回
    """

    def __init__(self, lst):
        # 构造传进来的list是一个引用，如果在外部对list进行修改会影响Vector的self._values
        self._values = list(lst)  # copy一份lst避免上述风险

    @classmethod
    def zero(cls, dim):
        """返回一个dim维度的零向量"""
        return cls([0] * dim)

    def __getitem__(self, index):
        """获取向量的某一维度"""
        return self._values[index]

    def __len__(self):
        """返回向量维度"""
        return len(self._values)

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error is adding, Length of vectors must be same."
        # return Vector([a + b for a, b in zip(self._values, other._values)])
        # 使用迭代器避免调用私有变量other._values
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error is subtracting, Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """返回数量乘法的结果向量 self * k """
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量 k * self """
        return self * k

    def __pos__(self):
        """数量乘法特殊情况：返回向量取正"""
        return 1 * self

    def __neg__(self):
        """数量乘法特殊情况：返回向量取负"""
        return -1 * self

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
