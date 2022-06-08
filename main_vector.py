from playLA.Vector import Vector

if __name__ == "__main__":
    lst = [5, 2, 1, 3, 4]
    vec = Vector(lst)
    print(vec)
    print(len(vec))
    for i in range(0, len(lst)):
        print("vec[{}] = {}".format(i, vec[i]), end=" ")
    print(repr(vec))

    vec1 = Vector([5, 3])
    vec2 = Vector([2, 1])
    vec3 = Vector([4, 2])

    print("{} + {} = {}".format(vec1, vec2, vec1 + vec2))
    print("{} - {} = {}".format(vec1, vec2, vec1 - vec2))
    print("{} * {} = {}".format(vec3, 3, vec3 * 3))
    print("{} * {} = {}".format(3, vec3, 3 * vec3))
    print("+{} = {}".format(vec3, +vec3))
    print("-{} = {}".format(vec3, -vec3))
