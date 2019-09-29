#!/usr/bin/python3
'''
Docstring. Short and simple.
Floyd algorythm
'''
import numpy as np

TIMES, N, X = (eval(i.split('=')[1]) for i in input().split(', '))
W = np.zeros((N, N))
W.fill(-5)
for i in TIMES:
    W[i[0] - 1, i[1] - 1] = i[2]

MAX = W.max() + 2 # not to influence
W = np.where(W == -5, MAX, W)

for k in range(N):
    for i in range(N):
        for j in range(N):
            W[i, j] = min(W[i, j], W[i, k] + W[k, j])
W = np.where(W == MAX, 0, W)

for i in range(N):
    if W[X-1, i] == 0 and i != X - 1:
        print(-1)
        break
else:
    print(W[X - 1].max())
