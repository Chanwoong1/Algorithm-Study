import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, S, D = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
answer = 0

for _ in range(N - 1) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(curr, prev) :
    global answer
    max_d = 0
    for next in graph[curr] :
        if next != prev :
            max_d = max(max_d, dfs(next, curr))
    if max_d >= D :
        answer += 1
    return max_d + 1
            
dfs(S, 0)
print((answer - 1) * 2 if answer else 0)