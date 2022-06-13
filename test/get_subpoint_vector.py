"""向量点乘的应用"""

from playLA.Vector import Vector

if __name__ == "__main__":
    """
    求向量v在向量u上的投影点坐标
    """
    v = Vector([5, 2])
    u = Vector([2, 5])

    # 投影点的距离 原点到投影点的距离
    d = u.dot(v) / u.norm()
    # 投影点的方向 即u向量的单位向量
    uu = u.normalize()
    # 投影点的坐标等于方向*距离
    p = d * uu

    print(p)
