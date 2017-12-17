import numpy as np

def solve1(num):
    corner = int(np.ceil(np.sqrt(num)))
    if corner % 2 == 0:
        corner += 1 # what square number is at the corner?

    spiral = (corner + 1) / 2 # which spiral is it?
    space = corner ** 2 - num
    sidelength = corner
    dist = space - corner
    return corner + dist

def getsmallestprime(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return 2
    i = 3
    while i < (num):
        if num % i == 0:
            return i
        else:
            i += 2
    return num


def solve2(num):
    a = []
    a.append(1)
    a.append(1)
    n = 2
    while a[-1] < num:
        a.append(a[-1] + a[getsmallestprime(n)-1])
        n += 1
    return a[-1]

if __name__ == '__main__':
    print(solve1(325489))
    print(solve2(325489))
    pass
