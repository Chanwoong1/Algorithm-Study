import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [0] * (N + 1)
E = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
    
for i in range(N + 1) :
    E[i].sort()

cnt = 1

def dfs(R) :
    global cnt
    visited[R] = cnt
    for i in E[R] :
        if (visited[i] == 0) :
            cnt += 1
            dfs(i)
            
dfs(R)            
print(*visited[1 : ], sep = '\n')