# https://www.acmicpc.net/problem/10986

N, M = list(map(int, input().split()))
lst = [i % M for i in list(map(int, input().split()))]
prepix = [0 for _ in range(M)]
presum = 0
prepix[0] = 1
for i in range(N) :
    presum += lst[i]
    prepix[presum % M] += 1
ans = 0
for i in prepix:
    ans += i * (i - 1) // 2
print(ans)