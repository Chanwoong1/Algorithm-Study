import sys
mod = 1000000007
res = 1
N, M = map(int, input().split())
N, M = min(N, M), max(N, M)
if N == 1:
    print(1)
    sys.exit(0)
prime = [True] * (N + 1)
for i in [2] + list(range(3, N + 1, 2)):
    if prime[i]:
        for j in range(i ** 2, N + 1, i if i == 2 else 2 * i):
            prime[j] = False
        cur = i
        tmp = 0
        while cur <= N:
            tmp += (N // cur) * (M // cur)
            cur *= i
        res *= pow(i, tmp, mod)
        res %= mod
print(res)