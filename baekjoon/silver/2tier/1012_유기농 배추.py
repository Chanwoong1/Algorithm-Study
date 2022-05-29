# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)

def dfs(x, y) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N) :
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for _ in range(T) :
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K) :
        X, Y = map(int, input().split())
        graph[X][Y] = 1
    answer = 0
    for x in range(M) :
        for y in range(N) :
            if graph[x][y] > 0 :
                dfs(x, y)
                answer += 1
    print(answer)