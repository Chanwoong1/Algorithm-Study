# https://www.acmicpc.net/problem/1246

N, M = map(int, input().split())
lst = sorted([int(input()) for _ in range(M)])
max_p = max_b = 0
for i in range(M) :
    t = lst[i] * ((M - i) if M - i <= N else N)
    if max_b < t:
        max_b = t
        max_p = lst[i]
print(max_p, max_b)