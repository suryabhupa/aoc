import numpy as np

def solve1(fname):
    contents = []
    with open(fname) as f:
        contents = f.readlines()
    c = [int(e.strip()) for e in contents]
    total = 0
    new_idx, idx = 0, 0
    while idx < len(c) or idx < 0:
        try:
            new_idx += c[idx]
            c[idx] = c[idx] + 1
            total += 1
            idx = new_idx
        except:
            break

    return total

def solve2(fname):
    contents = []
    with open(fname) as f:
        contents = f.readlines()
    c = [int(e.strip()) for e in contents]
    total = 0
    new_idx, idx = 0, 0
    while idx < len(c) or idx < 0:
        try:
            new_idx += c[idx]
            c[idx] = c[idx] - 1 if c[idx] > 2 else c[idx] + 1
            total += 1
            idx = new_idx
        except:
            break

    return total

if __name__ == '__main__':
    fname = '5.txt'
    print(solve1(fname))
    print(solve2(fname))
