import copy
import numpy as np

l = [l.strip().split()[0] for l in open('input.txt', 'r').readlines()] 

# Part 1 
def get_arr(l):
  arr = [np.array([0, 0]) for _ in range(len(l[0]))]
  for i in l:
    for idx, j in enumerate(arr):
      if int(i[idx]) == 0:
        j[0] += 1
      else:
        j[1] += 1
  return arr

arr = get_arr(l)
gamma = int(''.join([str(np.argmax(arr_i)) for arr_i in arr]), 2)
eps = int(''.join([str(np.argmin(arr_i)) for arr_i in arr]), 2)
print(gamma, eps, gamma * eps)

# Part 2 
gamma_l = copy.deepcopy(l)
eps_l = copy.deepcopy(l) 
g_idx = e_idx = 0
while len(gamma_l) > 1 or len(eps_l) > 1:
  if len(gamma_l) > 1:
    g_arr = get_arr(gamma_l)
    gamma_l = list(filter(lambda x: int(x[g_idx]) == int(g_arr[g_idx][0] <= g_arr[g_idx][1]), gamma_l))
    g_idx += 1

  if len(eps_l) > 1: 
    e_arr = get_arr(eps_l)
    eps_l = list(filter(lambda x: int(x[e_idx]) == int(e_arr[e_idx][0] > e_arr[e_idx][1]), eps_l))
    e_idx += 1


final_gamma = int(str(gamma_l[0]), 2)
final_eps = int(str(eps_l[0]), 2)

print(final_gamma, final_eps, final_gamma * final_eps) 

