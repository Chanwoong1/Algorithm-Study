import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M, R = map(int, input().split())
visit = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N + 1) :
    graph[i].sort()

dq = deque([R])
visit[R] = 1
cnt = 2
while dq :
    R = dq.popleft()
    for i in graph[R] :
        if visit[i] == 0 :
            dq.append(i)
            visit[i] = cnt
            cnt += 1

print(*visit[1 : ], sep = '\n')