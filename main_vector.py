from playLA.Vector import Vector

if __name__ == "__main__":
    lst = [5, 2, 1, 3, 4]
    vec = Vector(lst)
    print(vec)
    print(len(vec))
    for i in range(0, len(lst)):
        print("vec[{}] = {}".format(i, vec[i]), end=" ")
    print(repr(vec))

    vec1 = Vector([5, 2])
    vec2 = Vector([3, 1])
    vec3 = Vector([4, 2])

    print("{} + {} = {}".format(vec1, vec2, vec1 + vec2))
    print("{} - {} = {}".format(vec1, vec2, vec1 - vec2))
    print("{} * {} = {}".format(vec3, 3, vec3 * 3))
    print("{} * {} = {}".format(3, vec3, 3 * vec3))
    print("+{} = {}".format(vec3, +vec3))
    print("-{} = {}".format(vec3, -vec3))

    zero2 = Vector.zero(2)
    print(zero2)
    # 任意向量+零向量等于它本身
    print("{} + {} = {}".format(vec1, zero2, vec1 + zero2))

    # 求模
    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    # 单位向量
    print("normalize({}) = {}".format(vec1, vec1.normalize()))
    print("normalize({}) = {}".format(vec2, vec2.normalize()))

    # 单位向量求模应该为1
    print(vec1.normalize().norm())
    print(vec2.normalize().norm())

    # 0向量的特殊异常处理
    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

    # 测试向量内积
    print(vec1.dot(vec2))
