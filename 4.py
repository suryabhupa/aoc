import numpy as np

def solve1(fname):
    contents = []
    with open(fname) as f:
        contents = f.readlines()
    contents = [e.strip().split() for e in contents]
    total = 0
    for c in contents:
        if sorted(list(c)) == sorted(list(set(c))):
            total += 1

    return total

def solve2(fname):
    contents = []
    with open(fname) as f:
        contents = f.readlines()
    contents = [e.strip().split() for e in contents]
    total = 0
    for c in contents:
        c = [str(sorted(list(i))) for i in c]
        if sorted(list(c)) == sorted(list(set(c))):
            total += 1

    return total

if __name__ == '__main__':
    fname = '4.txt'
    print(solve1(fname))
    print(solve2(fname))
