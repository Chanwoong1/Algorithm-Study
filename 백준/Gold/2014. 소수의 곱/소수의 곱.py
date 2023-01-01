import heapq
K, N = map(int, input().split())
pq = []
prime = list(map(int, input().split()))
[heapq.heappush(pq, i) for i in prime]
for i in range(N) :
    p1 = heapq.heappop(pq)
    for j in range(K) :
        heapq.heappush(pq, p1 * prime[j])
        if p1 % prime[j] == 0 :
            break
print(p1)