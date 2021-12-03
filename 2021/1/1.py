import numpy as np

# Part 1 
l = np.array([int(l.strip()) for l in open('input.txt', 'r').readlines()])
ans = sum(l[1:] - l[:-1] > 0)
print(ans)

# Part 2
m = np.stack([l, np.append([0], l[:-1]), np.append([0, 0], l[:-2])], axis=1)[2:]
m = np.sum(m, axis=1)
ans = sum(m[1:] - m[:-1] > 0)
print(ans)
