import numpy as np

# Part 1 
l = [(l.strip().split()) for l in open('input.txt', 'r').readlines()] 
x, y = 0, 0
for i in l:
  if i[0] == 'forward':
    x += int(i[1])
  elif i[0] == 'down':
    y += int(i[1])
  elif i[0] == 'up':
    y -= int(i[1])
print(x, y, x*y)


# Part 2
x, y, aim = 0, 0, 0
for i in l:
  if i[0] == 'forward':
    x += int(i[1])
    y += aim * int(i[1])
  elif i[0] == 'down':
    aim += int(i[1])
  elif i[0] == 'up':
    aim -= int(i[1])
print(x, y, x*y)


