# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
height = 0
answer = 10000000000000000
for i in range(257) :
    max = 0
    min = 0
    for x in range(N) :
        for y in range(M) :
            if graph[x][y] < i :
                min += (i - graph[x][y])
            else :
                max += (graph[x][y] - i)
    inventory = max + B
    if inventory < min :
        continue
    time = 2 * max + min
    if time <= answer :
        answer = time
        height = i
print(answer, height)