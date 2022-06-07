class Vector:

    def __init__(self, lst):
        self._values = lst

    def __getitem__(self, index):
        """获取向量的某一维度"""
        return self._values[index]

    def __len__(self):
        """向量维度"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __del__(self):
        print("\nReleased.\n")
