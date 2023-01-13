import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
for _ in range(N) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E) :
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    color_map = [-1] * (V + 1)
    for i in range(1, V + 1) :
        if color_map[i] != -1 :
            continue
        color_map[i] = 0
        dq = deque([i])
        while dq :
            curr = dq.popleft()
            for next in graph[curr] :
                if color_map[next] == -1 :
                    color_map[next] = (color_map[curr] + 1) % 2
                    dq.append(next)
    
    answer = True
    for i in range(1, V + 1) :
        color = color_map[i]
        for j in graph[i] :
            if color_map[j] == color :
                answer = False
    
    if answer :
        print("YES")
    else :
        print("NO")