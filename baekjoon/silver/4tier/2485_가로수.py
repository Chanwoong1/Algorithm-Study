# https://www.acmicpc.net/problem/2485

import sys
from math import gcd

input = sys.stdin.readline
lst = []
for _ in range(int(input())) :
    lst.append(int(input()))

dt = []
for i in range(1, len(lst)) :
    dt.append(lst[i] - lst[i - 1])

g = dt[0]
for j in range(1, len(dt)) :
    g = gcd(g, dt[j])

answer = 0
for i in dt :
    answer += i // g - 1
print(answer)