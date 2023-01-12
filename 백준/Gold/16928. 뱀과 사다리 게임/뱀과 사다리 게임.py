import heapq
import sys

sys.setrecursionlimit(10 ** 7)
N, M = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(N + M) :
    x, y = map(int, input().split())
    graph[x] = y

answer = []
visited = [1, 1] + [0] * 101
heapq.heappush(answer, (0, 1))
while 1 :
    tmp = heapq.heappop(answer)
    if tmp[1] == 100 :
        print(tmp[0])
        break
    if tmp[1] > 100 :
        continue
    for i in range(1, 7) :
        next = tmp[1] + i
        if next < 100 and next != graph[next] :
            next = graph[next]
        if next <= 100 and visited[next] == 0 :
            visited[next] = 1
            heapq.heappush(answer, (tmp[0] + 1, next))