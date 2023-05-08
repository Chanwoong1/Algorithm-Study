import math

lst = [[0] * 6, [0] * 6]
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    lst[S][Y - 1] += 1
total = 0
for i in range(2):
    for j in range(6):
        total += math.ceil(lst[i][j] / K)
print(total)
