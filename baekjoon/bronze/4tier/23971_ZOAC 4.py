# https://www.acmicpc.net/problem/23971

import math
H, W, N, M = map(int, input().split())
h = math.ceil(H / (N + 1))
w = math.ceil(W / (M + 1))
print(h * w)
