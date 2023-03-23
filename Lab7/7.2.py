import random
from time import time
population = [x for x in range(1_000_000)]


def randomList(size):
    """ generate random list"""
    # x = random.sample(population, length)
    # print(x)
    # return x
    return random.sample(population, size)


def O2isIntersect(a, b, c):
    # x = set(a)
    # y = set(b)
    # z = set(c)

    for i in a:  # N
        for j in b:  # N

            if i == j:  # + smth
                if i in c:
                    return True
                # for k in c:
                #     if i == k:
                #         return True

    return False


def O3isIntersect(a, b, c):

    for i in a:  # N
        for j in b:  # N
            for k in c:  # N

                # print(".", end=" ")
                if i == j == k:
                    return True

    # N**3 + N
    return False


def main(size):
    a = randomList(size)
    b = randomList(size)
    c = randomList(size)

    s = time()
    print(O2isIntersect(a, b, c))
    e = time()
    print("O2 Elapse :", (e - s))

    # s = time()
    # print(O3isIntersect(a, b, c))
    # e = time()
    # print("O3 Elapse :", (e - s))


main(1_000_000)