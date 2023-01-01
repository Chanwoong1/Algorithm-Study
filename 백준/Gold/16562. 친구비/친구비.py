import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, k = map(int, input().split())
prices = list(enumerate(map(int, input().split()), start = 1))
prices.sort(key = lambda x : x[1])
prices = [(0, 0)] + prices
friends = [[] for _ in range(N + 1)]
for _ in range(M) :
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

total = 0
visited = [0 for _ in range(N + 1)]

def dfs(friend) :	# (1, 10)
    if len(friends[friend[0]]) == 0 :
        return
    for next in friends[friend[0]] :
        if visited[next] == 0 :
            visited[next] = 1
            for i in range(len(prices)) :
                if prices[i][0] == next :
                    dfs(prices[i])

for i in range(1, len(prices)) :
    if visited[prices[i][0]] == 0 :
        total += prices[i][1]
        visited[prices[i][0]] = 1
        dfs(prices[i])

if k - total < 0 :
    print("Oh no")
else :
    print(total)