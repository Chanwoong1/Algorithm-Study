import heapq
K, N = map(int, input().split())
pq = []
prime = list(map(int, input().split()))
[heapq.heappush(pq, i) for i in prime]
for i in range(N) :
    p1 = heapq.heappop(pq)
    for p2 in prime :
        heapq.heappush(pq, p1 * p2)
        if p1 % p2 == 0 :
            break
print(p1)