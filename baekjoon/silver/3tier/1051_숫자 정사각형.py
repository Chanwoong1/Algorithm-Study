# https://www.acmicpc.net/problem/1051

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
answer = []
for i in range(10) :
    for row in range(len(graph)) :
        if str(i) in graph[row] :
            for idx in range(M) :
                if str(i) == graph[row][idx] :
                    tmp = 1
                    x = M - idx
                    y = N - row
                    if x > y :
                        for j in range(1, y) :
                            if graph[row][idx] == graph[row + j][idx] and graph[row][idx] == graph[row][idx + j] and graph[row][idx] == graph[row + j][idx + j] :
                                tmp = (j + 1) ** 2
                    else :
                        for j in range(1, x) :
                            if graph[row][idx] == graph[row + j][idx] and graph[row][idx] == graph[row][idx + j] and graph[row][idx] == graph[row + j][idx + j] :
                                tmp = (j + 1) ** 2
                    answer.append(tmp)
        else :
            answer.append(0)
print(max(answer))