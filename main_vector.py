from playLA.Vector import Vector

if __name__ == "__main__":
    lst = [5, 2, 1]
    vec = Vector(lst)
    print(vec)
    print(len(vec))
    for i in range(0, len(lst)):
        print("vec[{}] = {}".format(i, vec[i]), end=" ")
    print("\n")
    print(repr(vec))
    del vec
