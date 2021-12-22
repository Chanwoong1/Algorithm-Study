# https://www.acmicpc.net/problem/13305

N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_gas = gas[0]
answer = dist[0] * gas[0]
min_dist = 0
for i in range(1, N - 1) :
    if gas[i] < min_gas :
        answer += min_gas * min_dist
        min_dist = dist[i]
        min_gas = gas[i]
    else :
        min_dist += dist[i]
    
    if i == N - 2 :
        answer += min_gas * min_dist
print(answer)
