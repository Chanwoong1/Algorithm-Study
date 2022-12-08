graph = [[0] * 100 for _ in range(100)]
for _ in range(int(input())) :
    x, y = map(int, input().split())
    for i in range(10) :
        for j in range(10) :
            graph[x + i][y + j] = 1
print(sum([sum(i) for i in graph]))