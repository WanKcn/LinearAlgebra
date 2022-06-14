"""
使用numpy中与向量有关的运算和操作
"""
import numpy as np

if __name__ == "__main__":
    # 当前numpy的版本号
    print(np.__version__)

    # 向量
    vec = np.array([1, 2, 3])
    print(vec)

    # 零向量 float
    print(np.zeros(5))
    # 每个维度为1
    print(np.ones(3))
    # 每个维度满
    print(np.full(5, 123))

    # np.array的基本属性
    print(vec)
    print("size = ", vec.size)
    print("size = ", len(vec))
    print(vec[1])
    print(vec[-1])
    print(vec[0:2])

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec2, 2 * vec2))
    print("{} * {} = {}".format(vec2, 2, vec2 * 2))

    # 逐个元素的乘法
    vec3 = vec * vec2
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("sum = {}".format(sum(e for e in vec3)))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    # 求模 np.array设计一个函数
    norm = np.linalg.norm(vec)
    print(norm)
    # 向量归1化
    vec_normalize = vec / norm
    print("vec_normalize = ", vec_normalize)
    # 单位向量的模为1 如果/0 需要自己处理
    print(np.linalg.norm(vec_normalize))
