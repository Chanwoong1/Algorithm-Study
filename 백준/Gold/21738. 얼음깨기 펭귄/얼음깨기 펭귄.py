import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, S, P = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
lst = []
visited = [0] * (N + 1)
def dfs(curr, n) :
    if curr == P :
        lst.append(n)
        return
    visited[curr] = 1
    for i in graph[curr] :
        if visited[i] == 0 :
            dfs(i, n + 1)

for i in range(1, S + 1) :
    dfs(i, 0)
    
lst.sort()
print(N - lst[0] - lst[1] - 1)