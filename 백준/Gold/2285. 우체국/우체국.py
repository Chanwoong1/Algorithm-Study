import sys
input = sys.stdin.readline

graph = []
people = 0
for _ in range(int(input())) :
    X, A = map(int, input().split())
    graph.append((X, A))
    people += A

graph.sort(key = lambda x : x [0])

cnt = 0
for X, A in graph :
    cnt += A
    if cnt > people / 2 :
        print(X)
        break