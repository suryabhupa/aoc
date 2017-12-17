import numpy as np

def solve1(num):
    corner = np.floor(np.sqrt(num))
    if corner % 2 == 0:
        corner += 1
    spiral = (corner + 1) / 2
    print('corner', corner)
    print('spiral-1', spiral-1)
    print('space from corner', num - corner ** 2)


if __name__ == '__main__':
    print(solve1(325489))
